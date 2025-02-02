import React, { useState } from "react";

const ThemeSwitcher = () => {
  const [isDarkMode, setIsDarkMode] = useState(false);

  const toggleTheme = () => {
    setIsDarkMode(!isDarkMode);
    if (isDarkMode) {
      document.documentElement.style.setProperty("--bg-color", "#fff");
      document.documentElement.style.setProperty("--text-color", "#000");
    } else {
      document.documentElement.style.setProperty("--bg-color", "#111");
      document.documentElement.style.setProperty("--text-color", "#ffcc00");
    }
  };

  return (
    <button onClick={toggleTheme}>
      Switch to {isDarkMode ? "Light" : "Dark"} Mode
    </button>
  );
};

export default ThemeSwitcher;
