import { useState } from 'react'
import {BrowserRouter, Routes, Route} from 'react-router-dom'


import './App.css'

function App() {


  return (
    <BrowserRouter>
      <Routes>
        {/* <Route element={<MainClient setTheUser={setTheUser} />} path="/client"/> */}
        {/* <Route element={<ClientSingleWrapper />} path="/client/chat" /> */}
        {/* <Route element={<MainAdmin setTheUser={setTheUser} />} path="/admin"/> */}
        {/* <Route element={<AdminMultiWrapper />} path="/admin/chat" /> */}
        {/* <Route element={<MainSupport setTheUser={setTheUser} />} path="/"/> */}
        {/* <Route element={<GuestSingleWrapper />} path="/chat" /> */}
      </Routes>
    
    </BrowserRouter>
  )
}

export default App
