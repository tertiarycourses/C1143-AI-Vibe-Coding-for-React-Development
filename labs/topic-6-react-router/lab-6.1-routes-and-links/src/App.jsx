import { Routes, Route } from 'react-router-dom'
import RootLayout from './layouts/RootLayout'
import HomePage from './pages/HomePage'
import CoursesPage from './pages/CoursesPage'
import AboutPage from './pages/AboutPage'

// App no longer renders the page directly — it declares a route map. The one
// layout route (RootLayout) wraps three child routes; whichever URL matches
// renders into RootLayout's <Outlet/>. `index` is the route for "/" itself.
//
// The course detail page, login and the private dashboard arrive in the next
// labs; for now these three routes turn one long page into a real multi-page app.
export default function App() {
  return (
    <Routes>
      <Route path="/" element={<RootLayout />}>
        <Route index element={<HomePage />} />
        <Route path="courses" element={<CoursesPage />} />
        <Route path="about" element={<AboutPage />} />
      </Route>
    </Routes>
  )
}
