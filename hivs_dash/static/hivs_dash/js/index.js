

var app = new Vue({
    el: '#app',
    data: {
        clientsTotal: {count: null},
        dailyAquisition: {
            date: [],
            count: [],
            options: {
                maintainAspectRatio: false,
                scales: {
                    xAxes: [{
                        type: 'time',
                    }],
                    yAxes: [{
                        ticks: {
                            beginAtZero:true,
                        }
                    }]
                }
            }
        },
        thisMonthAquisition: {
            count: null,
            gender: {labels:[], data: []}
        },
        lastMonthAquisition: {
            count: null,
            gender: {labels:[], data: []}
        },
        map: {
            instance: null,
            base: {
                url: 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png',
                options: {
                    attribution: '© <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, © <a href="https://carto.com/attribution">CARTO</a></div>'
                }
            },
            level1: {
                data: null,
                options: {
                    weight: 2,
                    color: '#ECEFF1',
                    opacity: 1,
                    fillColor: '#FF0000',
                    fillOpacity: 1
                }
            },
            baseLayer: null,
            level1Layer: null
        },
    },

    methods: {
        initMap() {
            this.map.instance = L.map('clients-map').setView([0, 0], 7);
            this.map.baseLayer = L.tileLayer(this.map.base.url, this.map.base.options);
            this.map.baseLayer.addTo(this.map.instance);
        },

        initLayers() {
            this.map.level1Layer = L.choropleth(this.map.level1.data.results, {
                valueProperty: 'count',
                scale: ['white', '#17a2b8'],
                steps: 5,
                mode: 'q', // q for quantile, e for equidistant, k for k-means
                style: {
                    color: '#fff',
                    weight: 2,
                    fillOpacity: 0.7
                },
                onEachFeature: function(feature, layer) {
                    layer.bindPopup(
                        feature.properties.name + ': ' + feature.properties.count + ' clients')
                }
            }).addTo(this.map.instance);
            this.map.instance.fitBounds(this.map.level1Layer.getBounds());
        },
    },
    mounted () {
        var now = new Date();
        var lastMonth = new Date();
        lastMonth.setMonth(lastMonth.getMonth() - 1);

        // daily aquisitions
        axios
            .get(
                apiRoot + 'clients/profiles/count/', {
                params: {
                    group: 'acquisition_date',
                    ordering: 'acquisition_date',
                }
            })
            .then((response) => {
                response.data.forEach((obj) => {
                    this.dailyAquisition.date.push(obj.acquisition_date);
                    this.dailyAquisition.count.push(obj.count);
                })

            })
            .catch(error => {console.log(error)})

        // this month acquisition
        axios
            .get(
                apiRoot + 'clients/profiles/total/', {
                params: {
                    group: 'acquisition_date',
                    acquisition_date__month: now.getMonth() + 1,
                    acquisition_date__year: now.getFullYear(),
                    ordering: 'acquisition_date',
                }
            })
            .then((response) => {
                this.thisMonthAquisition.count = response.data.count;
            })
            .catch(error => {console.log(error)})

        // last month acquisition
        axios
            .get(
                apiRoot + 'clients/profiles/total/', {
                params: {
                    group: 'acquisition_date',
                    acquisition_date__month: lastMonth.getMonth() + 1,
                    acquisition_date__year: lastMonth.getFullYear(),
                    ordering: 'acquisition_date',
                }
            })
            .then((response) => {
                this.lastMonthAquisition.count = response.data.count;
            })
            .catch(error => {console.log(error)})

        // this month acquisition by gender
        axios
            .get(
                apiRoot + 'clients/profiles/count/', {
                params: {
                    group: 'gender__name',
                    acquisition_date__month: now.getMonth() + 1,
                    acquisition_date__year: now.getFullYear(),
                }
            })
            .then((response) => {
                response.data.forEach((obj) => {
                    this.thisMonthAquisition.gender.labels.push(obj.gender__name);
                    this.thisMonthAquisition.gender.data.push(obj.count);
                })
            })
            .catch(error => {console.log(error)})

        // last month acquisition by gender
        axios
            .get(
                apiRoot + 'clients/profiles/count/', {
                params: {
                    group: 'gender__name',
                    acquisition_date__month: lastMonth.getMonth() + 1,
                    acquisition_date__year: lastMonth.getFullYear(),
                }
            })
            .then((response) => {
                response.data.forEach((obj) => {
                    this.lastMonthAquisition.gender.labels.push(obj.gender__name);
                    this.lastMonthAquisition.gender.data.push(obj.count);
                })
            })
            .catch(error => {console.log(error)})

        // get administrative areas level 1
        axios
            .get(
                apiRoot + 'administrative/areas/related_count/', {
                params: {
                    level: 1,
                    by: 'profiles'
                }
            })
            .then((response) => {
                this.map.level1.data = response.data;
                this.initMap();
                this.initLayers();
            })
            .catch(error => {console.log(error)})

        // total clients
        axios
            .get(apiRoot + 'clients/profiles/total/')
            .then((response) => {
                this.clientsTotal = response.data;
            })
            .catch(error => {console.log(error)})

    }
})
