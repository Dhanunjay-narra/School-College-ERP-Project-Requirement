export interface User {
  id: string;
  email: string;
  first_name: string;
  last_name: string;
  full_name: string;
  role: string;
  roles: string[];
  tenant_id: string;
  department_id?: string;
  campus_id?: string;
}
