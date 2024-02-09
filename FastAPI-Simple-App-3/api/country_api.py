from fastapi import APIRouter, HTTPException
import requests

router = APIRouter()

@router.get("/countries")
async def get_countries():
    try:
        response = requests.get("https://restcountries.com/v3.1/all")
        response.raise_for_status()
        countries = response.json()
        return countries
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch countries: {str(e)}")