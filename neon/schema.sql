-- ===========================================================================
-- Cook & Bake Academy — Neon Postgres schema
--
-- ARCHITECTURE (three tiers). The browser NEVER talks to Postgres:
--
--     React (browser)  --fetch-->  /api/* (Vercel functions)  --sql-->  Neon
--
-- The connection string (DATABASE_URL) lives only in the serverless function's
-- environment. It is never bundled into the JS the browser downloads, so the
-- database password cannot leak, and every write goes through code you control.
--
-- Run once:  psql "$DATABASE_URL" -f neon/schema.sql
-- ===========================================================================

-- ---------------------------------------------------------------------------
-- 1. users — signup / login handled by /api/auth/*.
--    We store a bcrypt HASH, never the password itself. If this table leaked,
--    the hashes are still useless to an attacker.
-- ---------------------------------------------------------------------------
create table if not exists public.users (
  id            bigint generated always as identity primary key,
  email         text        not null unique,
  name          text        not null,
  password_hash text        not null,
  created_at    timestamptz not null default now()
);

-- ---------------------------------------------------------------------------
-- 2. courses — the public catalogue. Same columns as cookbake/src/data/courses.js,
--    so the components built in Topics 1-4 keep working when Topic 5 swaps the
--    hard-coded array for this table.
-- ---------------------------------------------------------------------------
create table if not exists public.courses (
  id         bigint generated always as identity primary key,
  code       text        not null unique,          -- BAK-101, CUL-201, ...
  slug       text        not null unique,
  title      text        not null,
  category   text        not null check (category in ('Bakery', 'Cooking')),
  level      text        not null check (level in ('Beginner', 'Intermediate', 'Advanced')),
  fee        numeric(8,2) not null check (fee >= 0),
  weeks      int         not null check (weeks > 0),
  campus     text        not null check (campus in ('Bakehouse', 'Culinary')),
  summary    text        not null,
  emoji      text        not null default '🍞',
  image      text        not null,                 -- unsplash photo id
  created_at timestamptz not null default now()
);

-- ---------------------------------------------------------------------------
-- 3. enrollments — one row per (user, course). The API sets user_id from the
--    verified JWT, so a caller cannot enroll somebody else.
-- ---------------------------------------------------------------------------
create table if not exists public.enrollments (
  id         bigint generated always as identity primary key,
  user_id    bigint      not null references public.users (id) on delete cascade,
  course_id  bigint      not null references public.courses (id) on delete cascade,
  status     text        not null default 'active'
               check (status in ('active', 'completed', 'cancelled')),
  notes      text,
  created_at timestamptz not null default now(),
  unique (user_id, course_id)
);

create index if not exists enrollments_user_id_idx on public.enrollments (user_id);

-- ---------------------------------------------------------------------------
-- 4. reviews — public to read, signed-in to write, one per user per course.
-- ---------------------------------------------------------------------------
create table if not exists public.reviews (
  id         bigint generated always as identity primary key,
  user_id    bigint      not null references public.users (id) on delete cascade,
  course_id  bigint      not null references public.courses (id) on delete cascade,
  rating     int         not null check (rating between 1 and 5),
  body       text        not null check (length(body) between 1 and 2000),
  created_at timestamptz not null default now(),
  unique (user_id, course_id)
);

create index if not exists reviews_course_id_idx on public.reviews (course_id);

-- ---------------------------------------------------------------------------
-- 5. Seed the catalogue — the same 20 courses as cookbake/src/data/courses.js.
--    Re-runnable: `on conflict (code) do nothing`.
-- ---------------------------------------------------------------------------
insert into public.courses (code, slug, title, category, level, fee, weeks, campus, summary, emoji, image)
values
  ('BAK-101', 'artisan-sourdough-bread-baking', 'Artisan Sourdough Bread Baking', 'Bakery', 'Beginner', 680, 4, 'Bakehouse', 'Grow your own starter, master hydration and bake a crackling open crumb loaf.', '🍞', '1589367920969-ab8e050bbb04'),
  ('BAK-102', 'french-pastry-and-viennoiserie', 'French Pastry & Viennoiserie', 'Bakery', 'Intermediate', 1480, 8, 'Bakehouse', 'Laminated dough, croissants, pain au chocolat and the classic French pastry canon.', '🥐', '1509440159596-0249088772ff'),
  ('BAK-103', 'wedding-cake-design-and-decoration', 'Wedding Cake Design & Decoration', 'Bakery', 'Advanced', 1280, 6, 'Bakehouse', 'Tiering, structural support, fondant work and sugar flowers for showpiece cakes.', '🎂', '1535141192574-5d4897c12636'),
  ('BAK-104', 'macaron-masterclass', 'Macaron Masterclass', 'Bakery', 'Intermediate', 420, 2, 'Bakehouse', 'Perfect feet, smooth shells and ganache fillings — the meringue method demystified.', '🍬', '1558326567-98ae2405596b'),
  ('BAK-105', 'chocolate-and-confectionery-making', 'Chocolate & Confectionery Making', 'Bakery', 'Intermediate', 760, 4, 'Bakehouse', 'Tempering, moulding, bonbons and truffles with real couverture chocolate.', '🍫', '1511381939415-e44015466834'),
  ('BAK-106', 'cupcake-and-cake-pops-workshop', 'Cupcake & Cake Pops Workshop', 'Bakery', 'Beginner', 220, 1, 'Bakehouse', 'A one-week crash course in moist sponges, buttercream piping and party treats.', '🧁', '1486427944299-d1955d23e34d'),
  ('BAK-107', 'bread-making-fundamentals', 'Bread Making Fundamentals', 'Bakery', 'Beginner', 480, 3, 'Bakehouse', 'Yeast, kneading, proofing and shaping — the foundation every baker needs first.', '🥖', '1549931319-a545dcf3bc73'),
  ('BAK-108', 'cookie-and-biscuit-baking', 'Cookie & Biscuit Baking', 'Bakery', 'Beginner', 180, 1, 'Bakehouse', 'Chewy, crisp or shortbread — how one dough ratio changes everything.', '🍪', '1499636136210-6f4ee915583e'),
  ('BAK-109', 'pie-and-tart-specialist', 'Pie & Tart Specialist', 'Bakery', 'Intermediate', 560, 3, 'Bakehouse', 'Blind baking, pâte sucrée, custards and fruit fillings that never turn soggy.', '🥧', '1535920527002-b35e96722eb9'),
  ('BAK-110', 'korean-and-asian-bakery', 'Korean & Asian Bakery', 'Bakery', 'Intermediate', 720, 4, 'Bakehouse', 'Milk bread, tangzhong, cream buns and the soft-crumb bakes of Seoul and Tokyo.', '🍮', '1558961363-fa8fdf82db35'),
  ('CUL-201', 'italian-cuisine-mastery', 'Italian Cuisine Mastery', 'Cooking', 'Intermediate', 1180, 6, 'Culinary', 'Fresh pasta by hand, risotto, ragù and regional classics from Naples to Milan.', '🍝', '1551183053-bf91a1d81141'),
  ('CUL-202', 'thai-street-food-cooking', 'Thai Street Food Cooking', 'Cooking', 'Beginner', 540, 3, 'Culinary', 'Pound your own curry paste and balance the sour, salty, sweet and spicy.', '🍜', '1559314809-0d155014e29e'),
  ('CUL-203', 'japanese-sushi-and-sashimi', 'Japanese Sushi & Sashimi', 'Cooking', 'Intermediate', 980, 4, 'Culinary', 'Shari rice, fish selection, filleting and nigiri technique from a sushi chef.', '🍣', '1579871494447-9811cf80d66c'),
  ('CUL-204', 'french-culinary-foundations', 'French Culinary Foundations', 'Cooking', 'Beginner', 1580, 8, 'Culinary', 'Stocks, the five mother sauces, and the classical technique everything builds on.', '🥘', '1414235077428-338989a2e8c0'),
  ('CUL-205', 'chinese-wok-cooking', 'Chinese Wok Cooking', 'Cooking', 'Beginner', 520, 3, 'Culinary', 'Seasoning a wok, controlling the heat and chasing wok hei on a home stove.', '🥡', '1525755662778-989d0524087e'),
  ('CUL-206', 'indian-curry-and-spices', 'Indian Curry & Spices', 'Cooking', 'Beginner', 500, 3, 'Culinary', 'Blooming whole spices, building masalas and cooking regional curries from scratch.', '🍛', '1505253758473-96b7015fcd40'),
  ('CUL-207', 'healthy-meal-prep-and-nutrition', 'Healthy Meal Prep & Nutrition', 'Cooking', 'Beginner', 360, 2, 'Culinary', 'Batch cooking, macro balance and a week of lunches you will actually eat.', '🥗', '1490645935967-10de6ba17061'),
  ('CUL-208', 'vegetarian-and-vegan-cuisine', 'Vegetarian & Vegan Cuisine', 'Cooking', 'Beginner', 540, 3, 'Culinary', 'Plant proteins, umami without meat, and dairy-free sauces that still taste rich.', '🥦', '1512621776951-a57141f2eefd'),
  ('CUL-209', 'grilling-and-bbq-mastery', 'Grilling & BBQ Mastery', 'Cooking', 'Intermediate', 460, 2, 'Culinary', 'Direct and indirect heat, rubs, brines and low-and-slow smoking.', '🔥', '1555939594-58d7cb561ad1'),
  ('CUL-210', 'knife-skills-and-kitchen-essentials', 'Knife Skills & Kitchen Essentials', 'Cooking', 'Beginner', 160, 1, 'Culinary', 'Grip, julienne, brunoise and honing — one week that speeds up every dish after it.', '🔪', '1556909212-d5b604d0c90d')
on conflict (code) do nothing;
