// Static team data. In a bigger app this would come from a table too, but it is
// fine to hardcode content that never changes at runtime.
const chefs = [
  {
    id: 1,
    name: 'Chef Amélie Laurent',
    emoji: '👩‍🍳',
    role: 'Head of Bakery',
    bio: 'Fifteen years in Paris pâtisseries. Teaches sourdough, viennoiserie and cake work.',
  },
  {
    id: 2,
    name: 'Chef Kenji Watanabe',
    emoji: '🍣',
    role: 'Head of Cuisine',
    bio: 'Trained in Tokyo, then ran a Michelin-listed kitchen. Teaches sushi and knife skills.',
  },
  {
    id: 3,
    name: 'Chef Priya Nair',
    emoji: '🌶️',
    role: 'Regional Cuisine Lead',
    bio: 'Spice specialist. Teaches Indian curries, Thai street food and wok cooking.',
  },
]

export default function Chefs() {
  return (
    <div className="features">
      {chefs.map((chef) => (
        <article key={chef.id} className="feature">
          <div className="feature__icon">{chef.emoji}</div>
          <h3>{chef.name}</h3>
          <p className="chef__role">{chef.role}</p>
          <p className="muted">{chef.bio}</p>
        </article>
      ))}
    </div>
  )
}
