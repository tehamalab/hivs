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
            reportType: 'referral',
            dateRange: {start: '', end: ''},
            reports: {
                referral: {
                    label: 'area referrals',
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
                    label: 'area and gender',
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
                    label: 'area and age',
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
                },
                ageRange0151824100: {
                    label: 'area and age range 15-17, 18-24',
                    link: '',
                    uri: apiRoot + 'prevention/pivot/count',
                    params: {
                        by: ['related_areas', 'age'],
                        area_level: 1,
                        rows: 'area_name',
                        columns: ['age_range'],
                        values: ['count'],
                        format: 'csv',
                        totals: 'total',
                        pivot_type: 'age_range',
                        range_limits: '0,15,18,24,100',
                        range_labels: '15-,15-17,18-24,24+',
                        filename: 'by-age-range-15-17_18-24.csv'
                    }
                },
                ageRange0152024100: {
                    label: 'area and age range 15-19, 20-24',
                    link: '',
                    uri: apiRoot + 'prevention/pivot/count',
                    params: {
                        by: ['related_areas', 'age'],
                        area_level: 1,
                        rows: 'area_name',
                        columns: ['age_range'],
                        values: ['count'],
                        format: 'csv',
                        totals: 'total',
                        pivot_type: 'age_range',
                        range_limits: '0,15,20,24,100',
                        range_labels: '15-,15-19,20-24,24+',
                        filename: 'by-age-range-15-19_20-24.csv'
                    }
                },
                genderAgeRange0151824100: {
                    label: 'area and gender and age range 15-17, 18-24',
                    link: '',
                    uri: apiRoot + 'prevention/pivot/count',
                    params: {
                        by: ['related_areas', 'age', 'gender__name'],
                        area_level: 1,
                        rows: 'area_name',
                        columns: ['age_range', 'gender__name'],
                        values: ['count'],
                        format: 'csv',
                        totals: 'total',
                        pivot_type: 'age_range',
                        range_limits: '0,15,18,24,100',
                        range_labels: '15-,15-17,18-24,24+',
                        filename: 'by-gender-age-range-15-17_18-24.csv'
                    }
                },
                genderAgeRange0152024100: {
                    label: 'area and gender and age range 15-19, 20-24',
                    link: '',
                    uri: apiRoot + 'prevention/pivot/count',
                    params: {
                        by: ['related_areas', 'age', 'gender__name'],
                        area_level: 1,
                        rows: 'area_name',
                        columns: ['age_range', 'gender__name'],
                        values: ['count'],
                        format: 'csv',
                        totals: 'total',
                        pivot_type: 'age_range',
                        range_limits: '0,15,20,24,100',
                        range_labels: 'less than 15,15-19,20-24,24+',
                        filename: 'by-gender-age-range-15-19_20-24.csv'
                    }
                },
            }
            
        },

        condom: {
            link: '',
            reportType: 'centers',
            dateRange: {start: '', end: ''},
            reports: {
                centers: {
                    label: 'condom distribution per center',
                    link: '',
                    uri: apiRoot + 'condom/distributions/sum',
                    params: {
                        by: ['center__name'],
                        format: 'csv',
                        filename: 'condom_distributions_per_center.csv'
                    }
                },
                gender: {
                    label: 'condom distribution per client gender',
                    link: '',
                    uri: apiRoot + 'condom/distributions/sum',
                    params: {
                        by: ['gender__name'],
                        format: 'csv',
                        filename: 'condom_distributions_per_gender.csv'
                    }
                },
                age: {
                    label: 'condom distribution per age',
                    link: '',
                    uri: apiRoot + 'condom/distributions/sum',
                    params: {
                        by: ['age'],
                        format: 'csv',
                        filename: 'condom_distributions_per_age.csv'
                    }
                },
                date: {
                    label: 'condom distribution per date',
                    link: '',
                    uri: apiRoot + 'condom/distributions/sum',
                    params: {
                        by: ['date'],
                        format: 'csv',
                        filename: 'condom_distributions_per_date.csv'
                    }
                },
                attendanceType: {
                    label: 'condom Ddistribution per attendance type',
                    link: '',
                    uri: apiRoot + 'condom/distributions/sum',
                    params: {
                        by: ['attendance_type__name'],
                        format: 'csv',
                        filename: 'condom_distributions_per_attendance_type.csv'
                    }
                },
                purpose: {
                    label: 'condom distribution per purpose',
                    link: '',
                    uri: apiRoot + 'condom/distributions/sum',
                    params: {
                        by: ['purpose__name'],
                        format: 'csv',
                        filename: 'condom_distributions_per_purpose.csv'
                    }
                },
                centersGender: {
                    label: 'condom distribution per center and gender',
                    link: '',
                    uri: apiRoot + 'condom/pivot/sum',
                    params: {
                        by: ['center__name', 'gender__name'],
                        rows: 'center__name',
                        columns: ['gender__name'],
                        values: ['condoms_count'],
                        format: 'csv',
                        totals: 'total',
                        pivot_type: 'gender',
                        filename: 'condom_distributions_per_center_and_gender.csv'
                    }
                },
                centersAttendance: {
                    label: 'condom distribution per center and attendance type',
                    link: '',
                    uri: apiRoot + 'condom/pivot/sum',
                    params: {
                        by: ['center__name', 'attendance_type__name'],
                        rows: 'center__name',
                        columns: ['attendance_type__name'],
                        values: ['condoms_count'],
                        format: 'csv',
                        totals: 'total',
                        filename: 'condom_distributions_per_center_and_attendance_type.csv'
                    }
                },
                centersPurpose: {
                    label: 'condom distribution per center and purpose',
                    link: '',
                    uri: apiRoot + 'condom/pivot/sum',
                    params: {
                        by: ['center__name', 'purpose__name'],
                        rows: 'center__name',
                        columns: ['purpose__name'],
                        values: ['condoms_count'],
                        format: 'csv',
                        totals: 'total',
                        filename: 'condom_distributions_per_center_and_purpose.csv'
                    }
                },
            },
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
            var service = _.find(this.services.results, {'id': this.prevention.service});

            params.services = this.prevention.service
            params.date__gte = this.prevention.dateRange.start
            params.date__lte = this.prevention.dateRange.end

            // filename = service name report_type date_lte date_gte
            params.filename = slugify([
                service.name,
                this.prevention.reports[this.prevention.reportType].label,
                params.date__lte,
                'to',
                params.date__gte
            ].join('-')) + '.csv'

            this.prevention.link = uri + '?' + Qs.stringify(params, { indices: false })
        },

        /** Update condom distribution report link. */
        updateCondomReportLink() {
            var uri = this.condom.reports[this.condom.reportType].uri
            var params = JSON.parse(JSON.stringify(this.condom.reports[this.condom.reportType].params));

            params.date__gte = this.condom.dateRange.start
            params.date__lte = this.condom.dateRange.end

            // filename = service name report_type date_lte date_gte
            params.filename = slugify([
                this.condom.reports[this.condom.reportType].label,
                params.date__lte,
                'to',
                params.date__gte
            ].join('-')) + '.csv'

            this.condom.link = uri + '?' + Qs.stringify(params, { indices: false })
        },
    },

    mounted () {
        var date = new Date();
        var monthStart = new Date(date.getFullYear(), date.getMonth(), 1);
        var monthEnd = new Date(date.getFullYear(), date.getMonth() + 1, 0);

        this.prevention.dateRange.start = monthStart;
        this.prevention.dateRange.end = monthEnd;
        this.condom.dateRange.start = monthStart;
        this.condom.dateRange.end = monthEnd;

        this.getServices();
        this.baywatch([
                'prevention.service',
                'prevention.reportType',
                'prevention.dateRange.start',
                'prevention.dateRange.end',
            ], this.updatePreventionReportLink.bind(this));

        this.baywatch([
                'condom.reportType',
                'condom.dateRange.start',
                'condom.dateRange.end',
            ], this.updateCondomReportLink.bind(this));
    }

})
