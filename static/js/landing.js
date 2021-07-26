const timeLine = gsap.timeline({defaults: {ease: 'power1.out'}});
timeLine.to('.rocket', {transformOrigin: "right center", rotation: -30})
timeLine.fromTo(".rocket", { xPercent: 40, y: 50}, {x: 100, y: -800, duration: 3, ease: "none" });
timeLine.to('.intro', {y: "-100%", duration: 1}, "-=1");