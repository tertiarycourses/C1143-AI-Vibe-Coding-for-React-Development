-- ---------------------------------------------------------------------------
-- reviews — the MINI-CAPSTONE table (Lab 6.6).
--
--     You add this table, and the whole feature that uses it, mostly on your own
--     by vibe-coding. It is deliberately the same shape as `enrollments`, so the
--     pattern you already understand carries straight over:
--       - ANYONE may READ reviews (they are public, like the catalogue) — the
--         GET /api/reviews function calls no requireAuth().
--       - Only a SIGNED-IN user may WRITE, and only their OWN row — the POST and
--         DELETE functions read the user id from the verified JWT and put it in
--         the SQL themselves (`where ... and user_id = ${userId}`).
--     `unique (user_id, course_id)` gives one review per user per course, and
--     `rating` is constrained to 1..5 so a bad value is rejected at the database,
--     not just in the form.
--
-- Security lives in the API, not in the browser and not in a database policy.
-- What stops you touching someone else's row is the ownership check the
-- serverless function writes into every statement (`and user_id = ${userId}`),
-- where the user id comes from the verified token.
--
-- This block is already part of neon/schema.sql. If you ran that once against
-- your database in Topic 5, the table exists. It is reproduced here so you can
-- see the exact shape the useReviews hook and the /api/reviews functions expect.
-- ---------------------------------------------------------------------------
create table if not exists public.reviews (
  id         bigint generated always as identity primary key,
  user_id    bigint      not null references public.users (id) on delete cascade,
  course_id  bigint      not null references public.courses (id) on delete cascade,
  rating     int         not null check (rating between 1 and 5),
  body       text        not null check (length(body) between 1 and 2000),
  created_at timestamptz not null default now(),
  unique (user_id, course_id)   -- one review per user per course
);

create index if not exists reviews_course_id_idx on public.reviews (course_id);
