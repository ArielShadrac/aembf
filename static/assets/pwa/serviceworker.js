self.addEventListener('install',
    function(event){
        console.log('Service Worker Installing');
    });

self.addEventListener('fetch',
    function(event){
        event.respondWidth(
            caches.match(event.request).then(function(response){
                return response || 
                fetch(event.request);
            })
        );
    });   