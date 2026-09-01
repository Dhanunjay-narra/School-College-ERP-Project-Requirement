# Enterprise Security Architecture & Threat Model

## 1. Identity & Authentication Architecture
- **Password Storage**: PBKDF2-HMAC-SHA256 with 100,000 rounds and per-user cryptographic salt (Argon2 / BCrypt supported).
- **Token Security**: Cryptographically signed JWT tokens with standard expiration (60-minute access token, 7-day refresh token).
- **MFA / 2FA**: RFC 6238 Time-based One-Time Password (TOTP) algorithm supported across all privileged administrator personas.
- **Account Protection**: Progressive lockout mechanism with maximum 5 failed attempts triggering a 15-minute temporary lockout.

## 2. Multi-Tenant Partitioning & Data Isolation
All database queries enforce strict tenant boundary filtering (`tenant_id`). Cross-tenant leakage is prevented via:
1. Application middleware injection of validated tenant contexts from JWT claims.
2. Repository-level mandatory tenant query constraints.
3. Database level row-level security (RLS) policies in PostgreSQL.
