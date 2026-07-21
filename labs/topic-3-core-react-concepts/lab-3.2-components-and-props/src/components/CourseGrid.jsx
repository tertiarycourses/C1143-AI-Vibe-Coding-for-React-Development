import CourseCard from './CourseCard'

// Six cards, hand-written. Every card is the same component with a different object.
// Notice how repetitive and error-prone this is — one typo per card, six chances to get a
// number wrong, and only six of the twenty real courses shown. Lab 3.3 deletes all of this
// and replaces it with courses.map() over the full catalogue in src/data/courses.js.
export default function CourseGrid() {
  return (
    <div className="grid">
      <CourseCard
        course={{
          id: 1,
          code: 'BAK-101',
          slug: 'artisan-sourdough-bread-baking',
          emoji: '🍞',
          title: 'Artisan Sourdough Bread Baking',
          category: 'Bakery',
          level: 'Beginner',
          weeks: 4,
          fee: 680,
          campus: 'Bakehouse',
          summary: 'Grow your own starter, master hydration and bake a crackling open crumb loaf.',
        }}
      />
      <CourseCard
        course={{
          id: 2,
          code: 'BAK-102',
          slug: 'french-pastry-and-viennoiserie',
          emoji: '🥐',
          title: 'French Pastry & Viennoiserie',
          category: 'Bakery',
          level: 'Intermediate',
          weeks: 8,
          fee: 1480,
          campus: 'Bakehouse',
          summary: 'Laminated dough, croissants, pain au chocolat and the classic French pastry canon.',
        }}
      />
      <CourseCard
        course={{
          id: 4,
          code: 'BAK-104',
          slug: 'macaron-masterclass',
          emoji: '🍬',
          title: 'Macaron Masterclass',
          category: 'Bakery',
          level: 'Intermediate',
          weeks: 2,
          fee: 420,
          campus: 'Bakehouse',
          summary: 'Perfect feet, smooth shells and ganache fillings — the meringue method demystified.',
        }}
      />
      <CourseCard
        course={{
          id: 11,
          code: 'CUL-201',
          slug: 'italian-cuisine-mastery',
          emoji: '🍝',
          title: 'Italian Cuisine Mastery',
          category: 'Cooking',
          level: 'Intermediate',
          weeks: 6,
          fee: 1180,
          campus: 'Culinary',
          summary: 'Fresh pasta by hand, risotto, ragù and regional classics from Naples to Milan.',
        }}
      />
      <CourseCard
        course={{
          id: 13,
          code: 'CUL-203',
          slug: 'japanese-sushi-and-sashimi',
          emoji: '🍣',
          title: 'Japanese Sushi & Sashimi',
          category: 'Cooking',
          level: 'Intermediate',
          weeks: 4,
          fee: 980,
          campus: 'Culinary',
          summary: 'Shari rice, fish selection, filleting and nigiri technique from a sushi chef.',
        }}
      />
      <CourseCard
        course={{
          id: 20,
          code: 'CUL-210',
          slug: 'knife-skills-and-kitchen-essentials',
          emoji: '🔪',
          title: 'Knife Skills & Kitchen Essentials',
          category: 'Cooking',
          level: 'Beginner',
          weeks: 1,
          fee: 160,
          campus: 'Culinary',
          summary: 'Grip, julienne, brunoise and honing — one week that speeds up every dish after it.',
        }}
      />
    </div>
  )
}
