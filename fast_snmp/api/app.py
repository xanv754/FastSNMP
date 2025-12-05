import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fast_snmp.api.routes.device import SNMPRouter as DeviceRouter
from fast_snmp.api.routes.HUAWEI.olt import SNMPRouter as HuaweiOLTRouter
from fast_snmp.api.routes.UBIQUITI.olt import SNMPRouter as UbiquitiOLTRouter
from fast_snmp.api.routes.ZTE.olt import SNMPRouter as ZTEOLTRouter
from fast_snmp.api.routes.CISCO.snmp_system import SNMPRouter as SystemRouter
from fast_snmp.api.routes.CISCO.snmp_if import SNMPRouter as IFRouter


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

app.include_router(router=DeviceRouter, prefix=f"{VERSION_API}/device", tags=["device"])
app.include_router(
    router=HuaweiOLTRouter,
    prefix=f"{VERSION_API}/olt/huawei-mib",
    tags=["huawei-olt-mib"],
)
app.include_router(
    router=UbiquitiOLTRouter,
    prefix=f"{VERSION_API}/olt/ubiquiti-mib",
    tags=["ubiquiti-olt-mib"],
)
app.include_router(
    router=ZTEOLTRouter, prefix=f"{VERSION_API}/olt/zte-mib", tags=["zte-olt-mib"]
)
app.include_router(
    router=SystemRouter,
    prefix=f"{VERSION_API}/cisco/system-mib",
    tags=["cisco-system-mib"],
)
app.include_router(
    router=IFRouter, prefix=f"{VERSION_API}/cisco/if-mib", tags=["cisco-if-mib"]
)


@app.get("/")
def home():
    return {"detail": "Service is running..."}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
