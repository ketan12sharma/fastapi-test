from fastapi import APIRouter, HTTPException
from models.request import NestedListSumRequest
from models.response import NestedListSumResponse
from services.addition_service import process_addition
from datetime import datetime
import logging

addition_router = APIRouter()
logger = logging.getLogger(__name__)

@addition_router.post("/add", response_model=NestedListSumResponse)
async def add_numbers(request: NestedListSumRequest):
    started_at = datetime.utcnow()
    logger.info(f"Processing batch: {request.batchid}")

    try:
        result = process_addition(request.payload)
        completed_at = datetime.utcnow()

        response = NestedListSumResponse(
            batchid=request.batchid,
            response=result,
            status="complete",
            started_at=started_at,
            completed_at=completed_at
        )
        logger.info(f"Batch {request.batchid} processed successfully.")
        return response
    except Exception as e:
        logger.error(f"Error processing batch {request.batchid}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")