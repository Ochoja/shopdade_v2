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
        5: 'repeat(auto-fit, minmax(230px, 1fr))',
        4: 'repeat(auto-fit, minmax(200px, 1fr))',
        3: 'repeat(auto-fit, minmax(160px, 1fr))',
        category: '1fr 1fr 1fr'
      }
    }
  },
  plugins: []
}
