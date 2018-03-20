// 啟用 reveal.js
Reveal.initialize({
    controls: true,
    progress: true,
    history: true,
    center: true,
    keyboard: true,
    slideNumber: true,
    overview: true,

    transition: 'slide', // none/fade/slide/convex/concave/zoom
    // 加入一些 reveal.js 的外掛
    menu: {
        numbers: true,
        /*custom: [
            { title: 'More', icon: '<i class="fa fa-external-link"></i>', src: '../../plugin/menu/more.html' }
        ],*/
        transitions: false
    },
    chalkboard: { // font-awesome.min.css must be available
        toggleChalkboardButton: { left: "80px" },
        toggleNotesButton: { left: "130px" },
        theme: "chalkboard",
        color: ['rgba(255,255,0,1)', 'rgba(255,255,255,0.5)'],
    },
    dependencies: [
      {
          src: '../../plugin/highlight/highlight.js',
          async: true, condition: function () {
              return !!document.querySelector('pre code');
          }, callback: function () {
              hljs.initHighlightingOnLoad();
          }
      }, {
          src: '../../plugin/markdown/marked.js',
          condition: function () {
              return !!document.querySelector('[data-markdown]');
          }
      }, {
          src: '../../plugin/markdown/markdown.js',
          condition: function () {
              return !!document.querySelector('[data-markdown]');
          }
      }, {
          src: '../../plugin/menu/menu.js'
      }, {
          src: '../../plugin/chalkboard/chalkboard.js'
      }
    ],
    keyboard: {
        67: function () { RevealChalkboard.toggleNotesCanvas() },	// toggle notes canvas when 'c' is pressed
        66: function () { RevealChalkboard.toggleChalkboard() },	// toggle chalkboard when 'b' is pressed
        46: function () { RevealChalkboard.clear() },	// clear chalkboard when 'DEL' is pressed
        8: function () { RevealChalkboard.reset() },	// reset chalkboard data on current slide when 'BACKSPACE' is pressed
        68: function () { RevealChalkboard.download() },	// downlad recorded chalkboard drawing when 'd' is pressed
    }
});