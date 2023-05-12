Ext.define('JointExpenses.view.main.Main', {
    extend: 'Ext.form.Panel',
    xtype: 'app-main',

    controller: 'main',
    viewModel: 'main',
    bodyPadding: 5,
    fullscreen: true,

    items: [{
        xtype: 'orderlist'
    }]
});
