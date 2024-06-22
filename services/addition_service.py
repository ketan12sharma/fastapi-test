import multiprocessing
from typing import List
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def add_numbers(numbers: List[int]) -> int:
    return sum(numbers)

def process_addition(payload: List[List[int]]) -> List[int]:
    try:
        with multiprocessing.Pool() as pool:
            results = pool.map(add_numbers, payload)
        return results
    except Exception as e:
        logger.error(f"Error in process_addition: {str(e)}")
        raise