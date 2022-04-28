"""
Teacher Module
"""

from fastapi import APIRouter

router = APIRouter(
    tags=["Teacher"],
    prefix="/teacher"
)
