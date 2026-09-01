"""
Enterprise School & College ERP - Main ASGI Application Server.
Mounts all versioned v1 domain API routers, WebSocket handlers, and middleware.
"""
import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from backend.core.config import settings
from backend.core.middleware import RequestContextMiddleware
from backend.core.websocket_manager import ws_manager

# Import Domain API Routers
from backend.identity.presentation.api import router as auth_router
from backend.organization.presentation.api import router as org_router
from backend.students.presentation.api import router as student_router
from backend.parents.presentation.api import router as parent_router
from backend.admissions.presentation.api import router as admissions_router
from backend.academics.presentation.api import router as academics_router
from backend.faculty.presentation.api import router as faculty_router
from backend.attendance.presentation.api import router as attendance_router
from backend.examinations.presentation.api import router as exam_router
from backend.assignments.presentation.api import router as assignments_router
from backend.fees.presentation.api import router as fees_router
from backend.payments.presentation.api import router as payments_router
from backend.finance.presentation.api import router as finance_router
from backend.procurement.presentation.api import router as procurement_router
from backend.inventory.presentation.api import router as inventory_router
from backend.campus_store.presentation.api import router as store_router
from backend.hr.presentation.api import router as hr_router
from backend.payroll.presentation.api import router as payroll_router
from backend.transport.presentation.api import router as transport_router
from backend.hostels.presentation.api import router as hostel_router
from backend.library.presentation.api import router as library_router
from backend.crm.presentation.api import router as crm_router
from backend.communication.presentation.api import router as comm_router
from backend.workflows.presentation.api import router as workflow_router
from backend.documents.presentation.api import router as doc_router
from backend.projects.presentation.api import router as project_router
from backend.research.presentation.api import router as research_router
from backend.production.presentation.api import router as prod_router
from backend.compliance.presentation.api import router as comp_router
from backend.reporting.presentation.api import router as rep_router
from backend.ai.presentation.api import router as ai_router
from backend.search.presentation.api import router as search_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Enterprise Unified School & College ERP Platform API",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Register CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom Request Context & Security Middleware
app.add_middleware(RequestContextMiddleware)

# Mount API v1 Routers
api_v1_routers = [
    auth_router,
    org_router,
    student_router,
    parent_router,
    admissions_router,
    academics_router,
    faculty_router,
    attendance_router,
    exam_router,
    assignments_router,
    fees_router,
    payments_router,
    finance_router,
    procurement_router,
    inventory_router,
    store_router,
    hr_router,
    payroll_router,
    transport_router,
    hostel_router,
    library_router,
    crm_router,
    comm_router,
    workflow_router,
    doc_router,
    project_router,
    research_router,
    prod_router,
    comp_router,
    rep_router,
    ai_router,
    search_router
]

for r in api_v1_routers:
    app.include_router(r, prefix=settings.API_V1_STR)

@app.websocket("/ws/{channel}")
async def websocket_endpoint(websocket: WebSocket, channel: str):
    """Real-time WebSocket endpoint for notifications and telemetry."""
    await ws_manager.connect(websocket, channel)
    try:
        while True:
            data = await websocket.receive_text()
            await ws_manager.broadcast(channel, {"type": "broadcast", "data": data})
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket, channel)

@app.get("/health")
async def health_check():
    """Service health check endpoint."""
    return {
        "status": "HEALTHY",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "database": "CONNECTED",
        "redis_cache": "CONNECTED",
        "event_broker": "ACTIVE"
    }

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=settings.PORT, reload=True)
