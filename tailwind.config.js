/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'darked' : '#171725',
        'whitening' : '#FFFFFF',
        'graying' : '#92929D',
      },
      screen: {
        'sm' : '300px',
        'md' : '768px',
        'lg' : '1024px'
      }
    },
    fontFamily: {
      abc : ["Roboto", "sans-serif"],
    }
  },
  plugins: [],
}
