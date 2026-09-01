import { jsx as _jsx, jsxs as _jsxs } from "react/jsx-runtime";
import { useState } from "react";
import { OneClickLoginBar, DEMO_USERS } from "./components/OneClickLoginBar";
import { Sidebar } from "./components/Sidebar";
import { Header } from "./components/Header";
import { DashboardView } from "./components/DashboardView";
import { DataModuleView } from "./components/DataModuleView";
export function App() {
    const [currentUser, setCurrentUser] = useState(DEMO_USERS[0]);
    const [activeTab, setActiveTab] = useState("dashboard");
    const handleSelectRole = (roleData) => {
        setCurrentUser(roleData);
    };
    const renderContent = () => {
        switch (activeTab) {
            case "dashboard":
                return _jsx(DashboardView, { userRole: currentUser.role });
            case "students":
                return _jsx(DataModuleView, { moduleName: "Students", title: "Student Information & Lifecycle", description: "Manage active students, academic history, roll numbers, and enrollment records.", endpoint: "/students/" });
            case "academics":
                return _jsx(DataModuleView, { moduleName: "Courses", title: "Curriculum, Courses & Timetable", description: "Academic course catalogs, semester credits, faculty assignments, and schedules.", endpoint: "/academics/courses" });
            case "attendance":
                return _jsx(DataModuleView, { moduleName: "Attendance", title: "Smart Attendance Engine Logs", description: "Biometric smart gate scans, QR code validations, and subject attendance records.", endpoint: "/attendance/logs" });
            case "examinations":
                return _jsx(DataModuleView, { moduleName: "Examinations", title: "Examination Schedules & Hall Allocations", description: "Midterm and end-semester timetables, invigilators, and grade points.", endpoint: "/examinations/schedules" });
            case "fees":
                return _jsx(DataModuleView, { moduleName: "Fee Invoices", title: "Fees, Invoicing & Billing Engine", description: "Tuition fee structures, installments, concessions, and paid receipts.", endpoint: "/fees/invoices" });
            case "finance":
                return _jsx(DataModuleView, { moduleName: "Chart of Accounts", title: "Finance & General Ledger", description: "Standard double-entry chart of accounts, debits, credits, and trial balance.", endpoint: "/finance/chart-of-accounts" });
            case "hr":
                return _jsx(DataModuleView, { moduleName: "Employees", title: "HR & Employee Directory", description: "Faculty and non-teaching employee profiles, contracts, and leave balances.", endpoint: "/hr/employees" });
            case "library":
                return _jsx(DataModuleView, { moduleName: "Library Catalog", title: "Central Library MARC21 / ISBN Catalog", description: "Book titles, authors, shelf locations, RFID barcodes, and copy availability.", endpoint: "/library/books" });
            case "hostels":
                return _jsx(DataModuleView, { moduleName: "Hostel Rooms", title: "Hostel, Housing & Bed Allocation", description: "Residence blocks, room numbers, occupancy, and air-conditioning status.", endpoint: "/hostels/rooms" });
            case "transport":
                return _jsx(DataModuleView, { moduleName: "Bus Routes", title: "Transport Fleet & Live GPS Routes", description: "Bus route schedules, stops, driver contacts, and real-time coordinates.", endpoint: "/transport/routes" });
            case "inventory":
                return _jsx(DataModuleView, { moduleName: "Purchase Orders", title: "Procurement & Purchase Orders", description: "Requisitions, vendor RFQs, purchase orders, and goods receipt tracking.", endpoint: "/procurement/purchase-orders" });
            case "workflows":
                return _jsx(DataModuleView, { moduleName: "Workflows", title: "Multi-Tier Approval Workflow Engine", description: "Configurable purchase, leave, and admission approval pipelines.", endpoint: "/workflows/pending" });
            case "ai":
                return _jsx(DataModuleView, { moduleName: "AI Insights", title: "AI / ML Predictive Intelligence", description: "Automated dropout risk prediction, fee collection forecast, and workload analytics.", endpoint: "/ai/insights" });
            case "compliance":
                return _jsx(DataModuleView, { moduleName: "Audit Logs", title: "Compliance & Immutable Audit Logs", description: "Immutable audit trail of all transactions, timestamps, and actor IP addresses.", endpoint: "/compliance/audit-logs" });
            case "organization":
                return _jsx(DataModuleView, { moduleName: "Campuses", title: "Multi-Campus Facilities & Infrastructure", description: "Institution campuses, engineering blocks, lecture halls, and laboratories.", endpoint: "/organization/campuses" });
            default:
                return _jsx(DashboardView, { userRole: currentUser.role });
        }
    };
    return (_jsxs("div", { className: "min-h-screen flex flex-col bg-slate-100 text-slate-900 font-sans", children: [_jsx(OneClickLoginBar, { onSelectRole: handleSelectRole, activeRole: currentUser.role }), _jsxs("div", { className: "flex flex-1", children: [_jsx(Sidebar, { activeTab: activeTab, setActiveTab: setActiveTab, userRole: currentUser.role }), _jsxs("div", { className: "flex-1 flex flex-col min-w-0", children: [_jsx(Header, { user: currentUser }), _jsx("main", { className: "flex-1 p-6 overflow-y-auto max-w-7xl w-full mx-auto", children: renderContent() })] })] })] }));
}
export default App;
