import { Routes, Route, Navigate } from 'react-router-dom'
import RootLayout from './layouts/RootLayout'
import HomePage from './pages/HomePage'
import CoursesPage from './pages/CoursesPage'
import CourseDetailPage from './pages/CourseDetailPage'
import AboutPage from './pages/AboutPage'
import LoginPage from './pages/LoginPage'
import DashboardPage from './pages/DashboardPage'
import MyCoursesPage from './pages/dashboard/MyCoursesPage'
import ProfilePage from './pages/dashboard/ProfilePage'
import NotFoundPage from './pages/NotFoundPage'
import ProtectedRoute from './components/ProtectedRoute'

// The whole route map of the app lives here. Nesting mirrors the URL:
// every <Route> inside RootLayout renders into RootLayout's <Outlet/>.
export default function App() {
  return (
    <Routes>
      <Route path="/" element={<RootLayout />}>
        <Route index element={<HomePage />} />
        <Route path="courses" element={<CoursesPage />} />
        <Route path="courses/:slug" element={<CourseDetailPage />} />
        <Route path="about" element={<AboutPage />} />
        <Route path="login" element={<LoginPage />} />

        {/* Everything inside this pathless route is auth-gated. */}
        <Route element={<ProtectedRoute />}>
          <Route path="dashboard" element={<DashboardPage />}>
            <Route index element={<Navigate to="my-courses" replace />} />
            <Route path="my-courses" element={<MyCoursesPage />} />
            <Route path="profile" element={<ProfilePage />} />
          </Route>
        </Route>

        {/* Catch-all: any URL that matched nothing above renders the 404. */}
        <Route path="*" element={<NotFoundPage />} />
      </Route>
    </Routes>
  )
}
