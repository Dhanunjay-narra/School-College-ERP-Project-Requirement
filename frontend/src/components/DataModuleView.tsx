import React, { useState, useEffect } from "react";
import { Plus, Download, Search, RefreshCw } from "lucide-react";
import { fetchApi } from "../services/api";

export const DataModuleView = ({ moduleName, title, description, endpoint }: any) => {
  const [data, setData] = useState<any[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [search, setSearch] = useState<string>("");

  useEffect(() => {
    async function loadData() {
      setLoading(true);
      const res = await fetchApi(endpoint);
      if (Array.isArray(res)) setData(res);
      else if (res && typeof res === "object") setData([res]);
      else setData([]);
      setLoading(false);
    }
    loadData();
  }, [endpoint]);

  return (
    <div className="space-y-4">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
        <div>
          <h2 className="text-lg font-bold text-slate-800">{title}</h2>
          <p className="text-xs text-slate-500 mt-0.5">{description}</p>
        </div>
        <div className="flex items-center space-x-2">
          <button className="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg border border-slate-200 text-xs font-semibold text-slate-600 hover:bg-slate-50">
            <Download className="w-3.5 h-3.5" />
            <span>Export CSV</span>
          </button>
          <button className="flex items-center space-x-1.5 px-3.5 py-1.5 rounded-lg bg-sky-600 hover:bg-sky-700 text-xs font-semibold text-white">
            <Plus className="w-3.5 h-3.5" />
            <span>Add Record</span>
          </button>
        </div>
      </div>

      <div className="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden">
        <div className="p-3.5 border-b border-slate-200 flex items-center justify-between gap-3">
          <div className="relative flex-1 max-w-sm">
            <Search className="w-3.5 h-3.5 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
            <input
              type="text"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              placeholder={`Filter ${moduleName}...`}
              className="w-full bg-slate-50 border border-slate-200 pl-8 pr-3 py-1.5 rounded-lg text-xs focus:outline-none focus:ring-1 focus:ring-sky-500"
            />
          </div>
          <span className="text-xs text-slate-400 font-medium">{data.length} records active</span>
        </div>

        <div className="overflow-x-auto">
          {loading ? (
            <div className="p-8 text-center text-xs text-slate-400 flex items-center justify-center space-x-2">
              <RefreshCw className="w-4 h-4 animate-spin text-sky-500" />
              <span>Fetching live records from ERP database...</span>
            </div>
          ) : data.length === 0 ? (
            <div className="p-8 text-center text-xs text-slate-400">No records found. Click "Add Record" to create one.</div>
          ) : (
            <table className="w-full text-left text-xs">
              <thead className="bg-slate-50 text-slate-700 font-semibold border-b border-slate-200">
                <tr>
                  {Object.keys(data[0]).map((k) => (
                    <th key={k} className="py-2.5 px-4 capitalize">{k.replace(/_/g, ' ')}</th>
                  ))}
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100 text-slate-700">
                {data.map((row, idx) => (
                  <tr key={idx} className="hover:bg-slate-50 transition-colors">
                    {Object.values(row).map((val: any, cIdx) => (
                      <td key={cIdx} className="py-2.5 px-4">
                        {typeof val === "object" ? JSON.stringify(val) : String(val)}
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
      </div>
    </div>
  );
};
