import React, {FC} from 'react'
import './App.css'
import {BrowserRouter, Route, Routes} from 'react-router-dom'
import MainLayout from './layouts/MainLayout'
import HomeView from './views/HomeView'
import TestView from './views/TestView'
import DrouotView from './views/DrouotView'


const App: FC = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MainLayout/>}>
          <Route index element={<HomeView/>}/>
          <Route path="*" element={<HomeView/>}/>
          <Route path="test" element={<TestView/>}/>
          <Route path="drouot" element={<DrouotView/>}/>
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App