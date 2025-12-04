import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fast_snmp.api.routes.device import SNMPRouter as DeviceRouter
from fast_snmp.api.routes.HUAWEI.olt import SNMPRouter as HuaweiOLTRouter


VERSION_API = "/api/v1"
app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    router=DeviceRouter, 
    prefix=f"{VERSION_API}/device", 
    tags=["device"]
)
app.include_router(
    router=HuaweiOLTRouter, 
    prefix=f"{VERSION_API}/olt/huawei", 
    tags=["huawei-olt"]
)


@app.get("/")
def home():
    return {"detail": "Service is running..."}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
