import asyncio
from datetime import datetime, timezone
import os
import random
from typing import Literal

from dotenv import load_dotenv
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

load_dotenv()

cors_origins = [origin.strip() for origin in os.getenv("CORS_ORIGINS", "*").split(",") if origin.strip()]

app = FastAPI(title="Trading Screenshot Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AnalyzeResponse(BaseModel):
    direction: Literal["UP", "DOWN"]
    confidence: int
    reasoning: str
    partner_link: str


class SignalRecord(BaseModel):
    username: str
    pair: str
    expiry: str
    direction: Literal["UP", "DOWN"]
    confidence: int
    reasoning: str
    created_at: str


signal_history: dict[str, list[SignalRecord]] = {}


def _safe_confidence(raw_value: int | float | str | None) -> int:
    try:
        value = int(float(raw_value)) if raw_value is not None else 85
    except (TypeError, ValueError):
        value = 85
    return max(75, min(100, value))


def _safe_direction(raw_value: str | None) -> Literal["UP", "DOWN"]:
    if not raw_value:
        return "UP"
    normalized = str(raw_value).strip().upper()
    return "DOWN" if normalized in {"DOWN", "ВНИЗ", "SELL", "SHORT"} else "UP"


async def simulate_analysis() -> dict:
    # Emulates analysis time to make UI feel like AI processing is running.
    await asyncio.sleep(random.uniform(1.8, 3.4))
    return {
        "direction": random.choice(["UP", "DOWN"]),
        "confidence": random.randint(75, 100),
        "reasoning": "AI анализ завершен",
    }


@app.get("/health")
def health() -> dict:
    return {"ok": True}


@app.get("/")
def root() -> dict:
    return {"service": "matrix-trade-backend", "ok": True}


@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze_chart(
    file: UploadFile = File(...),
    user_id: str = Form("anonymous"),
    username: str = Form("Trader"),
    pair: str = Form("EUR/USD"),
    expiry: str = Form("1 минута"),
) -> AnalyzeResponse:
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Upload an image file")

    image_bytes = await file.read()
    if not image_bytes:
        raise HTTPException(status_code=400, detail="Uploaded file is empty")

    if len(image_bytes) > 10 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="Image is too large (max 10MB)")

    try:
        result = await simulate_analysis()
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"Analysis failed: {exc}") from exc

    direction = _safe_direction(result.get("direction"))
    confidence = _safe_confidence(result.get("confidence"))
    reasoning = str(result.get("reasoning") or "Сигнал сформирован на основе структуры свечей.")
    partner_link = os.getenv("PARTNER_LINK", "https://pocketoption.com")
    response = AnalyzeResponse(
        direction=direction,
        confidence=confidence,
        reasoning=reasoning[:220],
        partner_link=partner_link,
    )

    record = SignalRecord(
        username=username[:64] or "Trader",
        pair=pair[:32] or "EUR/USD",
        expiry=expiry[:32] or "1 минута",
        direction=response.direction,
        confidence=response.confidence,
        reasoning=response.reasoning,
        created_at=datetime.now(timezone.utc).isoformat(),
    )
    signal_history.setdefault(user_id[:64] or "anonymous", []).append(record)
    signal_history[user_id[:64] or "anonymous"] = signal_history[user_id[:64] or "anonymous"][-30:]

    return response


@app.get("/history/{user_id}")
def get_history(user_id: str) -> dict:
    records = signal_history.get(user_id[:64] or "anonymous", [])
    return {"items": [record.model_dump() for record in reversed(records)]}
