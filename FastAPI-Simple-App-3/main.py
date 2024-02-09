from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from api import country_api, user_api
from fastapi.middleware.cors import CORSMiddleware
from ml.k_means import perform_kmeans_clustering

app = FastAPI()

# API Routers
app.include_router(country_api.router, prefix="/api/v1")
app.include_router(user_api.router, prefix="/api/v1")

# CORS (Cross-Origin Resource Sharing) setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["localhost", "127.0.0.1"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"},
    )

@app.get("/api/v1/analysis", tags=["analysis"])
async def get_analysis():
    try:
        user_activity_data = user_api.generate_mock_activity_data(user_count=100)
        cluster_labels = perform_kmeans_clustering(user_activity_data)
        
        # Convert cluster_labels to a JSON-serializable format
        cluster_labels_json = list(map(int, cluster_labels))
        
        return {"cluster_labels": cluster_labels_json}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
