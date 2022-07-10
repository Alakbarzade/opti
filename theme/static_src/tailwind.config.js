/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        screens: {
            xs: '468px',
            sm: '600px',
            md: '768px',
            lg: '1024px',
            xl: '1280px',
            xxl: '1536px',
        },
        extend: {
            backgroundImage: {
                'prev': "url('/src/img/button-prev.svg')",
                'cargo': "url('/public/src/img/bg.png')",

            },
            animation: {
                'spin-slow': 'spin 30s linear infinite',
            },

            fontFamily: {
                Nunito: "'Nunito', serif",
            },
            colors: {
                primary: '#61A2F9',
                secondary: '#2E83F8',
                txtcolor: '#222222',
                third: '#3470C0',
                sliderbg1: 'rgba(30, 129, 135, 0.3) 30%',
                sliderbg2: 'rgba(255, 239, 152, 0.3) 100%',
                menu: 'rgb(255 255 255 / 92%)',
                langbar: 'rgb(0 0 0 / 50%);',
                langborder: 'rgba(72, 62, 200, 1)',
                langborder2: 'rgba(209, 66, 212, 1)',

                // ...
            },
            fill: {
                current: 'currentColor',
            },

            fill: theme => ({
                'red': theme('colors.red.500'),
                'green': theme('colors.green.500'),
                'blue': theme('colors.blue.500'),
            }),
            boxShadow: {
                sm: '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
                DEFAULT: '0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)',
                md: '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
                lg: '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
                xl: '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)',
                '2xl': '0 25px 50px -12px rgba(0, 0, 0, 0.25)',
                '3xl': '0 35px 60px -15px rgba(0, 0, 0, 0.3)',
                inner: 'inset 0 2px 4px 0 rgba(0, 0, 0, 0.06)',
                blue: '0 10px 15px -3px #61A2F9, 0 4px 6px -2px #61A2F9',
                yellow: '0 10px 15px -3px #FFD147, 0 4px 6px -2px #FFD147',
                red: '0 10px 15px -3px #DD636E, 0 4px 6px -2px #DD636E',
                green: '0 10px 15px -3px #74C766, 0 4px 6px -2px #74C766',
                gray: '0 10px 15px -3px #A8D3D8, 0 4px 6px -2px #A8D3D8',
                none: 'none',
            },
        },
    },
    variants: {
        extend: {
            boxShadow: ['blue'],
            fill: ['hover', 'focus'], // this line does the trick
        },

    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
