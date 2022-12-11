import {Link, Outlet} from 'react-router-dom'
import {FC} from 'react'

const MainLayout: FC = () => {
  return (
  <div>
    <header>
      <Link to="/home">Home</Link>&nbsp;
      <Link to="/test">Test</Link>&nbsp;
      <Link to="/drouot">Drouot</Link>
    </header>
    <div>
      <Outlet/>
    </div>
  </div>
  )
}

export default MainLayout