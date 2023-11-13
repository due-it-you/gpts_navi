import React from 'react';
import './App.css';
import Header from './Header';
import Footer from './Footer';

function App() {
  return (
    <div className="flex flex-col h-screen">
        <Header />
        <div className="flex-grow p-4">
            {/* ここにメインコンテンツ */}
        </div>
        <Footer />
    </div>
);
}

export default App;
