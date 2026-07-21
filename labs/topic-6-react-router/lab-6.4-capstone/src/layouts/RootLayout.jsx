import { Outlet } from 'react-router-dom'
import Navbar from '../components/Navbar'
import Footer from '../components/Footer'

// The app shell. Navbar and Footer render on every page; the active route's
// element renders wherever <Outlet/> sits.
export default function RootLayout() {
  return (
    <>
      <Navbar />
      <main style={{ minHeight: '70vh' }}>
        <Outlet />
      </main>
      <Footer />
    </>
  )
}
