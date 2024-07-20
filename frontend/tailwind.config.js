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
        hero: "url('./src/assets/images/hero.jpg')",
        footwear:
          "url('https://ik.imagekit.io/Ochoja01/shopDADE/footwear.png?updatedAt=1711169406807')",
        top: "url('https://ik.imagekit.io/Ochoja01/shopDADE/tops.png?updatedAt=1711169407303')",
        suit: "url('https://ik.imagekit.io/Ochoja01/shopDADE/suit.png?updatedAt=1711169407259')",
        bottom: "url('https://ik.imagekit.io/Ochoja01/shopDADE/pants.png?updatedAt=1711169407202')",
        jacket:
          "url('https://ik.imagekit.io/Ochoja01/shopDADE/jacket.png?updatedAt=1711169406932')",
        accesory:
          "url('https://ik.imagekit.io/Ochoja01/shopDADE/accesories.png?updatedAt=1711169406591')"
      },
      gridTemplateColumns: {
        5: 'repeat(auto-fit, minmax(230px, 1fr))',
        4: 'repeat(auto-fit, minmax(200px, 1fr))',
        3: 'repeat(auto-fit, minmax(160px, 1fr))',
        category: 'repeat(3, 1fr)'
      }
    }
  },
  plugins: []
}
