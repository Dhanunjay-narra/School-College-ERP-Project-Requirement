import React, { useState } from "react";
import { ShieldCheck, Users, TrendingUp, CheckCircle2, ArrowUpRight, Filter, Download, Plus, RefreshCw } from "lucide-react";

export const FacultyDashboard: React.FC = () => {
  const [loading, setLoading] = useState(false);

  return (
    <div className="space-y-6">
      <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <div className="inline-flex items-center space-x-2 px-2.5 py-0.5 rounded-full bg-sky-50 text-sky-700 text-xs font-semibold mb-2">
            <span>Specialized Workspace</span>
            <span>•</span>
            <span>Real-Time Sync</span>
          </div>
          <h1 className="text-xl font-extrabold text-slate-900">Faculty & Teacher Academic Workbench</h1>
          <p className="text-xs text-slate-500 mt-1 max-w-2xl">Class attendance marking, syllabus tracking, continuous assessment grades, and research publications.</p>
        </div>
        <div className="flex items-center space-x-2">
          <button className="flex items-center space-x-1 px-3 py-1.5 rounded-lg border border-slate-200 text-xs font-semibold text-slate-700 hover:bg-slate-50">
            <Download className="w-3.5 h-3.5" />
            <span>Export View</span>
          </button>
          <button className="flex items-center space-x-1 px-3.5 py-1.5 rounded-lg bg-sky-600 hover:bg-sky-700 text-xs font-semibold text-white">
            <Plus className="w-3.5 h-3.5" />
            <span>New Action</span>
          </button>
        </div>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs">
          <div className="text-xs font-semibold text-slate-500">Active Operational Units</div>
          <div className="text-2xl font-black text-slate-800 mt-1">100%</div>
          <div className="text-[11px] text-emerald-600 font-bold mt-1 flex items-center">
            <CheckCircle2 className="w-3 h-3 mr-1" /> All subsystems operational
          </div>
        </div>
        <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs">
          <div className="text-xs font-semibold text-slate-500">Service SLA Compliance</div>
          <div className="text-2xl font-black text-slate-800 mt-1">99.98%</div>
          <div className="text-[11px] text-sky-600 font-bold mt-1">Sub-second response time</div>
        </div>
        <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs">
          <div className="text-xs font-semibold text-slate-500">Audit Status</div>
          <div className="text-2xl font-black text-slate-800 mt-1">Verified</div>
          <div className="text-[11px] text-purple-600 font-bold mt-1">Immutable log stream active</div>
        </div>
      </div>

      <div className="bg-white rounded-xl border border-slate-200 shadow-xs p-5">
        <h3 className="font-bold text-sm text-slate-800 border-b border-slate-100 pb-3">Operational Stream & Records</h3>
        <div className="p-8 text-center text-xs text-slate-500">
          Viewing synchronized live operational feed for Faculty & Teacher Academic Workbench. All access events are cryptographically audited.
        </div>
      </div>
    </div>
  );
};

export default FacultyDashboard;
