/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    colors: {
      primary: '#EF233C',
      white: '#ffffff'
    },
    fontFamily: {
      logo: ['Rammetto One', 'sans-serif']
    },
    extend: {
      backgroundImage: {
        hero: "url('./src/assets/images/hero.jpg')"
      },
      gridTemplateColumns: {
        4: 'repeat(auto-fit, minmax(200px, 1fr))'
      }
    }
  },
  plugins: []
}
