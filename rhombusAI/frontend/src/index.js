import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Home from './pages/Home/'
import FileAnalysis from './pages/FileAnalysis'
import Error from './components/Error'

ReactDOM.render(
    <React.StrictMode>
        <Router>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/file-analysis/:fileID" element={<FileAnalysis />} />
                <Route path="*" element={<Error />} />
            </Routes>
        </Router>
    </React.StrictMode>,
    document.getElementById('root')
)