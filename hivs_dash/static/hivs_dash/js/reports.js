// reports.js

    var datepickerOptions = {
      sundayFirst: true
    }
    // install plugin
    Vue.use(window.AirbnbStyleDatepicker, datepickerOptions)


var app = new Vue({
    el: '#app',

    data: {
        services: null,
        prevention: {
            service: null,
            link: '',
            filename: '',
            reportType: 'referral',
            dateRange: {start: '', end: ''},
            reports: {
                referral: {
                    label: 'referrals',
                    link: '',
                    uri: apiRoot + 'prevention/pivot/count',
                    params: {
                        referral_made: '1',
                        by: ['related_areas', 'referral_successful'],
                        area_level: 1,
                        rows: 'area_name',
                        columns: ['referral_successful'],
                        values: ['count'],
                        format: 'csv',
                        totals: 'total',
                        pivot_type: 'referrals',
                        filename: 'referrals.csv'
                    }
                },
                gender: {
                    label: 'by gender',
                    link: '',
                    uri: apiRoot + 'prevention/pivot/count',
                    params: {
                        by: ['related_areas', 'gender__name'],
                        area_level: 1,
                        rows: 'area_name',
                        columns: ['gender__name'],
                        values: ['count'],
                        format: 'csv',
                        totals: 'total',
                        pivot_type: 'gender',
                        filename: 'by-gender.csv'
                    }
                },
                age: {
                    label: 'by age',
                    link: '',
                    uri: apiRoot + 'prevention/pivot/count',
                    params: {
                        by: ['related_areas', 'age'],
                        area_level: 1,
                        rows: 'area_name',
                        columns: ['age'],
                        values: ['count'],
                        format: 'csv',
                        totals: 'total',
                        pivot_type: 'age',
                        filename: 'by-age.csv'
                    }
                }
            }
            
        },

    },

    methods: {

        /** Watch multiple properties. */
        baywatch (props, watcher) {
            var iterator = function(prop) {
                this.$watch(prop, watcher);
            };
            props.forEach(iterator, this);
        }, 

        /** Fetch a list of available prevention services. */
        getServices() {
            axios
                .get(apiRoot + 'prevention/services', {params: {ordering: 'id'}})
                .then((response) => {
                    this.services = response.data;
                    this.selectService(this.services.results[0].id);
                })
                .catch(error => {console.log(error)})
            },

        /** Configure prevention services selection. */
        selectService(i) {
            this.prevention.service = i
            this.updatePreventionReportLink();
        },

        /** Update prevention services report link. */
        updatePreventionReportLink() {
            var uri = this.prevention.reports[this.prevention.reportType].uri
            var params = JSON.parse(JSON.stringify(this.prevention.reports[this.prevention.reportType].params));

            params.services = this.prevention.service
            params.date__gte = this.prevention.dateRange.start
            params.date__lte = this.prevention.dateRange.end

            this.prevention.link = uri + '?' + Qs.stringify(params, { indices: false })
        }
    },

    mounted () {
        var date = new Date();
        this.prevention.dateRange.start = new Date(date.getFullYear(), date.getMonth(), 1);
        this.prevention.dateRange.end = new Date(date.getFullYear(), date.getMonth() + 1, 0);

        this.getServices();
        this.baywatch([
                'prevention.service',
                'prevention.reportType',
                'prevention.dateRange.start',
                'prevention.dateRange.end',
            ], this.updatePreventionReportLink.bind(this));
            
    }

})
