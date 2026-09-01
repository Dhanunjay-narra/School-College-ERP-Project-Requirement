import React from "react";
import { Users, GraduationCap, DollarSign, CalendarCheck, ArrowUpRight, CheckCircle } from "lucide-react";

export const DashboardView = ({ userRole }: any) => {
  const stats = [
    { label: "Total Enrolled Students", value: "3,842", change: "+12.4%", icon: GraduationCap, color: "text-blue-600", bg: "bg-blue-50" },
    { label: "Faculty & Staff Members", value: "248", change: "+4.1%", icon: Users, color: "text-indigo-600", bg: "bg-indigo-50" },
    { label: "Fee Collection (YTD)", value: "₹12.85 Cr", change: "94.8%", icon: DollarSign, color: "text-emerald-600", bg: "bg-emerald-50" },
    { label: "Campus Attendance Rate", value: "94.2%", change: "+1.8%", icon: CalendarCheck, color: "text-cyan-600", bg: "bg-cyan-50" },
  ];

  return (
    <div className="space-y-6">
      <div className="bg-gradient-to-r from-sky-700 via-sky-800 to-indigo-900 rounded-2xl p-6 text-white shadow flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <div className="inline-flex items-center space-x-2 px-2.5 py-1 rounded-full bg-white/10 text-sky-200 text-xs font-medium mb-2">
            <span>Academic Year 2026-2027</span>
            <span>•</span>
            <span>Semester 4 Live</span>
          </div>
          <h1 className="text-2xl font-bold">Apex Institute of Technology & Management</h1>
          <p className="text-sky-100 text-xs mt-1">Autonomous University System • NAAC A++ Accredited</p>
        </div>
        <div className="bg-white/10 px-4 py-3 rounded-xl text-right">
          <div className="text-xs text-sky-200">System Security & Compliance</div>
          <div className="text-sm font-bold text-emerald-300 flex items-center justify-end space-x-1.5 mt-0.5">
            <CheckCircle className="w-4 h-4 text-emerald-400" />
            <span>100% Audit Verified</span>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        {stats.map((s, idx) => {
          const Icon = s.icon;
          return (
            <div key={idx} className="bg-white rounded-xl p-5 border border-slate-200 shadow-sm">
              <div className="flex items-center justify-between">
                <div className={`p-2.5 rounded-lg ${s.bg}`}>
                  <Icon className={`w-5 h-5 ${s.color}`} />
                </div>
                <span className="text-xs font-semibold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-full flex items-center">
                  <ArrowUpRight className="w-3 h-3 mr-0.5" />
                  {s.change}
                </span>
              </div>
              <div className="mt-3">
                <div className="text-2xl font-extrabold text-slate-800">{s.value}</div>
                <div className="text-xs text-slate-500 mt-0.5 font-medium">{s.label}</div>
              </div>
            </div>
          );
        })}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 bg-white rounded-xl p-5 border border-slate-200 shadow-sm space-y-4">
          <h3 className="font-bold text-sm text-slate-800 border-b border-slate-100 pb-3">Live Campus Operations & Academic Status</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            <div className="p-3.5 rounded-lg bg-slate-50 border border-slate-200">
              <div className="text-xs font-semibold text-slate-700">Today's Class Schedule (CS Dept)</div>
              <div className="text-xs text-slate-500 mt-1">CS401: Distributed Systems (RM-101)</div>
              <div className="mt-2 flex items-center justify-between text-[11px]">
                <span className="text-emerald-700 font-bold bg-emerald-100 px-2 py-0.5 rounded">Attendance: 94.2%</span>
                <span className="text-slate-400">09:00 - 10:00 AM</span>
              </div>
            </div>
            <div className="p-3.5 rounded-lg bg-slate-50 border border-slate-200">
              <div className="text-xs font-semibold text-slate-700">Campus Transport Fleet</div>
              <div className="text-xs text-slate-500 mt-1">12 Buses On Route • GPS Live</div>
              <div className="mt-2 flex items-center justify-between text-[11px]">
                <span className="text-sky-700 font-bold bg-sky-100 px-2 py-0.5 rounded">All Routes On Time</span>
                <span className="text-slate-400">ETA: 08:45 AM</span>
              </div>
            </div>
          </div>
        </div>

        <div className="bg-white rounded-xl p-5 border border-slate-200 shadow-sm space-y-4">
          <h3 className="font-bold text-sm text-slate-800 border-b border-slate-100 pb-3">AI Predictive Insights</h3>
          <div className="space-y-3">
            <div className="p-3 rounded-lg bg-indigo-50 border border-indigo-100">
              <div className="text-xs font-bold text-indigo-950">Student Dropout Risk: Minimal (1.6%)</div>
              <p className="text-[11px] text-slate-600 mt-1">Retention model indicates optimal engagement across all engineering branches.</p>
            </div>
            <div className="p-3 rounded-lg bg-emerald-50 border border-emerald-100">
              <div className="text-xs font-bold text-emerald-950">Fee Collection Forecast: 94.8%</div>
              <p className="text-[11px] text-slate-600 mt-1">Automated reminders projected to collect remaining dues smoothly.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
