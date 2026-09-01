import { jsx as _jsx, jsxs as _jsxs } from "react/jsx-runtime";
import { useState, useEffect } from "react";
import { Plus, Download, Search, RefreshCw } from "lucide-react";
import { fetchApi } from "../services/api";
export const DataModuleView = ({ moduleName, title, description, endpoint }) => {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [search, setSearch] = useState("");
    useEffect(() => {
        async function loadData() {
            setLoading(true);
            const res = await fetchApi(endpoint);
            if (Array.isArray(res))
                setData(res);
            else if (res && typeof res === "object")
                setData([res]);
            else
                setData([]);
            setLoading(false);
        }
        loadData();
    }, [endpoint]);
    return (_jsxs("div", { className: "space-y-4", children: [_jsxs("div", { className: "flex flex-col sm:flex-row sm:items-center justify-between gap-3 bg-white p-5 rounded-xl border border-slate-200 shadow-sm", children: [_jsxs("div", { children: [_jsx("h2", { className: "text-lg font-bold text-slate-800", children: title }), _jsx("p", { className: "text-xs text-slate-500 mt-0.5", children: description })] }), _jsxs("div", { className: "flex items-center space-x-2", children: [_jsxs("button", { className: "flex items-center space-x-1.5 px-3 py-1.5 rounded-lg border border-slate-200 text-xs font-semibold text-slate-600 hover:bg-slate-50", children: [_jsx(Download, { className: "w-3.5 h-3.5" }), _jsx("span", { children: "Export CSV" })] }), _jsxs("button", { className: "flex items-center space-x-1.5 px-3.5 py-1.5 rounded-lg bg-sky-600 hover:bg-sky-700 text-xs font-semibold text-white", children: [_jsx(Plus, { className: "w-3.5 h-3.5" }), _jsx("span", { children: "Add Record" })] })] })] }), _jsxs("div", { className: "bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden", children: [_jsxs("div", { className: "p-3.5 border-b border-slate-200 flex items-center justify-between gap-3", children: [_jsxs("div", { className: "relative flex-1 max-w-sm", children: [_jsx(Search, { className: "w-3.5 h-3.5 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" }), _jsx("input", { type: "text", value: search, onChange: (e) => setSearch(e.target.value), placeholder: `Filter ${moduleName}...`, className: "w-full bg-slate-50 border border-slate-200 pl-8 pr-3 py-1.5 rounded-lg text-xs focus:outline-none focus:ring-1 focus:ring-sky-500" })] }), _jsxs("span", { className: "text-xs text-slate-400 font-medium", children: [data.length, " records active"] })] }), _jsx("div", { className: "overflow-x-auto", children: loading ? (_jsxs("div", { className: "p-8 text-center text-xs text-slate-400 flex items-center justify-center space-x-2", children: [_jsx(RefreshCw, { className: "w-4 h-4 animate-spin text-sky-500" }), _jsx("span", { children: "Fetching live records from ERP database..." })] })) : data.length === 0 ? (_jsx("div", { className: "p-8 text-center text-xs text-slate-400", children: "No records found. Click \"Add Record\" to create one." })) : (_jsxs("table", { className: "w-full text-left text-xs", children: [_jsx("thead", { className: "bg-slate-50 text-slate-700 font-semibold border-b border-slate-200", children: _jsx("tr", { children: Object.keys(data[0]).map((k) => (_jsx("th", { className: "py-2.5 px-4 capitalize", children: k.replace(/_/g, ' ') }, k))) }) }), _jsx("tbody", { className: "divide-y divide-slate-100 text-slate-700", children: data.map((row, idx) => (_jsx("tr", { className: "hover:bg-slate-50 transition-colors", children: Object.values(row).map((val, cIdx) => (_jsx("td", { className: "py-2.5 px-4", children: typeof val === "object" ? JSON.stringify(val) : String(val) }, cIdx))) }, idx))) })] })) })] })] }));
};
