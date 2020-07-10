function sendRequest(url, method, data){
    var r = axios({
        method: method,
        url: url,
        data: data,
        xsrfCookieName: 'csrftoken',
        xsrfHeaderName: 'X-CSRFToken',
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    return r
}

var vigainput = new Vue({
    el: '#vigainput',
    data: {
        b: '',
        result: [],
        vigas: []
    },
    created(){
        var vm = this;
        var r = sendRequest('', 'get')
            .then(function(response){
                vm.vigas = response.data.vigas;
            })
    },
    methods: {
        dimensionar(){
            var vm = this;
            var formData = new FormData();
            formData.append('b', this.b);

            sendRequest('', 'get', formData)
                .then(function(response){
                    vm.result.push(response.data.b);
                })
        }
    }
})


/*
var vigainput = new Vue({
    el: '#vigainput',
    data: {
        viga: '',
        vigas: [
            { description: 'Viga 100'},
            { description: 'Viga 02'},
        ]
}
    created(){
        var vm = this;
        var r = sendRequest('', 'get')
            .then(function(response){
                vm.vigas = response.data.vigas;
            })
    },
    methods: {
        createViga(){
            var vm = this;
            var formData = new FormData();
            formData.append('description', this.vigas);

            sendRequest('', 'post', formData)
                .then(function(response){
                    vm.vigas.push(response.data.viga);
                    vm.viga = '';
                })
        }
    }
})
*/