

var app = new Vue({
    el: '#app',
    data: {
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
        }
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
    }
})
