import { Routes, Route } from 'react-router-dom'
import RootLayout from './layouts/RootLayout'
import HomePage from './pages/HomePage'
import CoursesPage from './pages/CoursesPage'
import CourseDetailPage from './pages/CourseDetailPage'
import AboutPage from './pages/AboutPage'
import NotFoundPage from './pages/NotFoundPage'

// Two new routes this lab: a dynamic segment (:slug) for the detail page, and
// the catch-all "*" that renders the 404 for anything that matched nothing else.
export default function App() {
  return (
    <Routes>
      <Route path="/" element={<RootLayout />}>
        <Route index element={<HomePage />} />
        <Route path="courses" element={<CoursesPage />} />
        <Route path="courses/:slug" element={<CourseDetailPage />} />
        <Route path="about" element={<AboutPage />} />
        <Route path="*" element={<NotFoundPage />} />
      </Route>
    </Routes>
  )
}
