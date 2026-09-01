import React from "react";
import { Bell, Search, Shield } from "lucide-react";

export const Header = ({ user }: any) => {
  return (
    <header className="bg-white border-b border-slate-200 px-6 py-3.5 flex items-center justify-between sticky top-[45px] z-40">
      <div className="flex items-center space-x-4 flex-1 max-w-lg">
        <div className="relative w-full">
          <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            placeholder="Search students, faculty, courses, books, fee invoices..."
            className="w-full bg-slate-100 border border-slate-200 pl-9 pr-4 py-1.5 rounded-lg text-xs focus:outline-none focus:ring-2 focus:ring-sky-500"
          />
        </div>
      </div>
      <div className="flex items-center space-x-4">
        <button className="relative p-2 text-slate-500 hover:text-slate-700 hover:bg-slate-100 rounded-full">
          <Bell className="w-4 h-4" />
          <span className="absolute top-1.5 right-1.5 w-2 h-2 bg-rose-500 rounded-full"></span>
        </button>
        <div className="flex items-center space-x-3 pl-3 border-l border-slate-200">
          <div className="w-8 h-8 rounded-full bg-sky-100 text-sky-800 flex items-center justify-center font-bold text-xs">
            {user.name.charAt(0)}
          </div>
          <div className="text-left hidden sm:block">
            <div className="text-xs font-bold text-slate-800">{user.name}</div>
            <div className="text-[11px] font-medium text-sky-600 flex items-center space-x-1">
              <Shield className="w-3 h-3 inline" />
              <span>{user.role}</span>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};
