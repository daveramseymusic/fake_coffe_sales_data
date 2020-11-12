


-- Unit sales per vairiants days for All data I have 2019-03 to 2019-10-10
with
    --set it up so you can see where theres only one sale per day of a coffee

    fluke_sales_setup as(
        --test
        /*select date(created_at_date) as creation_date, variant_name, count(variant_name) as units_sold, sum(net_sales) as net_sales
        from public.dave_retail_sandbox*/
        where item_name = 'Workshop Coffees'
          and expired = false
          and employee = false
          and customer_id is not null
          and created_at_date between '2019-03-01' and '2019-10-15'
        group by 1,2
        order by 1
    )
    -- ,
    --
--vpd as/*/*/*/**/*/*/*/(
select *
--            creation_date, variant_name, sum(units_sold) as unitss_old, sum(net_sales) as net_sales
from fluke_sales_setup
where units_sold > 2;
--)
selec t *
from vpd;
--,

     --
    vpd2 as(select creation_date, count(*)as variants_per_day, sum(units_sold) as total_ws_usold, round(sum(net_sales),2) as net_sales_pd
    from vpd
    group by 1
    order by 1)


--group by variants_per_day and count total # of units sold and count total sales
--divide everything by number of days
select variants_per_day, count(creation_date) as number_of_days, sum(total_ws_usold)/number_of_days as unit_sales_per_variants_day, sum(net_sales_pd)/number_of_days as net_sales_per_variants_day
from vpd2
group by variants_per_day
order by 3 desc;

--Unit sales per vairiants days for All data I have before the march crash
with
    vpd as(select created_at_date, variant_name, count(created_at) as units_sold, sum(net_sales) as net_sales
    from public.dave_retail_sandbox
    where item_name = 'Workshop Coffees'
                   and expired = false
                   and employee = false
                   and customer_id is not null
                    and created_at_date < '2020-03-01'
    group by created_at_date, variant_name
    order by 1,2),

    vpd2 as(select created_at_date, count(*)as variants_per_day, sum(units_sold) as total_ws_usold, round(sum(net_sales),2) as net_sales_pd
    from vpd
    group by created_at_date
    order by 1)

--group by variants_per_day and count total # of units sold and count total sales
--divide everything by number of days
select variants_per_day, count(created_at_date) as number_of_days, sum(total_ws_usold)/number_of_days as unit_sales_per_variants_day, sum(net_sales_pd)/number_of_days as net_sales_per_variants_day
from vpd2
group by variants_per_day
order by 3 desc;


--All Retail Coffee boxes -Unit sales per vairiants days for All data I have 2019-03 to 2019-10-10
with
    vpd as(select created_at_date, variant_name, count(created_at) as units_sold, sum(net_sales) as net_sales
    from public.dave_retail_sandbox
    where category_name = 'Retail Coffee'
                   and expired = false
                   and employee = false
                   and customer_id is not null
                    and created_at_date between '2019-03-01' and '2019-10-15'
    group by created_at_date, variant_name
    order by 1,2),

    vpd2 as(select created_at_date, count(*)as variants_per_day, sum(units_sold) as total_ws_usold, round(sum(net_sales),2) as net_sales_pd
    from vpd
    group by created_at_date
    order by 1)


--group by variants_per_day and count total # of units sold and count total sales
--divide everything by number of days
select variants_per_day, count(created_at_date) as number_of_days, sum(total_ws_usold)/number_of_days as unit_sales_per_variants_day, sum(net_sales_pd)/number_of_days as net_sales_per_variants_day
from vpd2
group by variants_per_day
order by 3 desc;


--ALL RETAIL BOXES Unit sales per vairiants days for All data I have
with
vpd as(select created_at_date, variant_name, count(created_at) as units_sold, sum(net_sales) as net_sales
from public.dave_retail_sandbox
where category_name = 'Retail Coffee'
               and expired = false
               and employee = false
               and customer_id is not null
                and created_at_date < '2020-03-01'
group by created_at_date, variant_name
order by 1,2),

vpd2 as(select created_at_date, count(*)as variants_per_day, sum(units_sold) as total_ws_usold, round(sum(net_sales),2) as net_sales_pd
from vpd
group by created_at_date
order by 1)


--group by variants_per_day and count total # of units sold and count total sales
--divide everything by number of days
select variants_per_day, count(created_at_date) as number_of_days, sum(total_ws_usold)/number_of_days as unit_sales_per_variants_day, sum(net_sales_pd)/number_of_days as net_sales_per_variants_day
from vpd2
group by variants_per_day
order by 3 desc;

--Including Crash ALL RETAIL BOXES Unit sales per vairiants days for All data I have
with
vpd as(select created_at_date, variant_name, count(created_at) as units_sold, sum(net_sales) as net_sales
from public.dave_retail_sandbox
where category_name = 'Retail Coffee'
               and expired = false
               and employee = false
               and customer_id is not null
group by created_at_date, variant_name
order by 1,2),

vpd2 as(select created_at_date, count(*)as variants_per_day, sum(units_sold) as total_ws_usold, round(sum(net_sales),2) as net_sales_pd
from vpd
group by created_at_date
order by 1)


--group by variants_per_day and count total # of units sold and count total sales
--divide everything by number of days
select variants_per_day, count(created_at_date) as number_of_days, sum(total_ws_usold)/number_of_days as unit_sales_per_variants_day, sum(net_sales_pd)/number_of_days as net_sales_per_variants_day
from vpd2
group by variants_per_day
order by 3 desc;






-- select * from public.dave_retail_sandbox where category_name = 'Retail Coffee'  limit 6