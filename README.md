LLM Shareable Quiz
Generate Quiz From User Promot on Users lecture material
Allow quiz to be shareable via link

---

# Requirements

## Functional Requirements

### 1. User Authentication

- Users can sign up and log in using Supabase Auth (email/password, OAuth, etc.).
- Users can sign in anonymously (anonymous auth) without providing credentials.
- Anonymous users get a unique UUID immediately after anonymous sign-in.
- Users can upgrade from anonymous to logged-in account without losing their UUID or data.

### 2. Quiz Creation & Management

- Anonymous or logged-in users can generate/create quizzes.
- Quizzes created by anonymous users are associated with their anonymous UUID.
- Logged-in users’ quizzes are associated with their real UUID.
- Logged-in users can generate a unique shareable link (slug) for each quiz.
- Users can retrieve quizzes by ID or shareable link.
- Users can update/delete only their own quizzes.

### 3. Quiz Taking & Submission

- Anyone with a quiz link (logged-in or anonymous) can take the quiz.
- Quiz submissions are stored with `user_id` set to UUID of user or anonymous user, or `NULL` if completely unauthenticated.
- Quiz submissions include user answers, score, and optional feedback.
- Anonymous users can submit quizzes without logging in.
- Logged-in users can view their past quiz attempts and results.

### 4. Data Access & Security

- RLS policies restrict editing and deletion of quizzes/submissions to their creators only.
- Public quizzes are readable by anyone with the shareable link.
- API endpoints validate tokens from Supabase Auth for logged-in and anonymous users.
- Rate limiting and spam protection on quiz creation and submission endpoints.

---

## Non-Functional Requirements

### 1. Security

- Use secure random unique identifiers (UUIDs and slugs) to prevent guessing.
- Protect all API endpoints with JWT token verification.
- Protect against spam with rate limiting or CAPTCHA on anonymous operations.

### 2. Performance & Scalability

- Backend (FastAPI) must handle concurrent quiz creations and submissions efficiently.
- Use Supabase as the primary database with proper indexing on quiz and submission IDs.
- Support fast retrieval of quizzes by ID or shareable link.

### 3. Maintainability

- Separate auth logic (handled on frontend with Supabase client) from business logic (FastAPI backend).
- Use clear, consistent API routes for quiz operations (`/quiz/create`, `/quiz/{id}`, `/quiz/{slug}/submit`).
- Implement RLS policies in Supabase for secure data access control.

### 4. Usability

- Anonymous users can start immediately without friction.
- Prompt users to sign up or log in only when needed (before saving or sharing).
- Shareable links must be user-friendly and unguessable.

---

# Flow (Text Diagram)

```plaintext
START
  │
  ▼
[User visits app]
  │
  ├─> (No auth) → Frontend calls
  │      supabase.auth.signInAnonymously()
  │         ↓
  │      User gets anonymous UUID
  │         ↓
  │      User creates quiz (FastAPI with anon UUID)
  │         ↓
  │      User takes quiz or shares link
  │
  ├─> (Optional) User chooses to sign up/log in
  │         ↓
  │      Frontend calls supabase.auth.signIn()
  │         ↓
  │      User upgraded from anon → logged-in UUID (same UUID)
  │         ↓
  │      User’s quizzes and submissions stay linked
  │         ↓
  │      User can share quizzes
  │
  ▼
[User or friends]
  │
  ├─> Anyone with shareable link accesses quiz (no auth needed)
  │         ↓
  │      Takes quiz → FastAPI saves submission with user_id (anon or logged-in UUID)
  │
  ▼
END
```

---

If you want, I can help you with detailed API spec or example requests/responses next!
