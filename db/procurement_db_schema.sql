PGDMP     4    8            	    z            Procurement_DB    14.4    14.4 ?    ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ?           1262    18041    Procurement_DB    DATABASE     t   CREATE DATABASE "Procurement_DB" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
     DROP DATABASE "Procurement_DB";
                eSmooothiee    false            ?            1259    20186    PPMP_costcenterbudget_seq    SEQUENCE     ?   CREATE SEQUENCE public."PPMP_costcenterbudget_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 99999999
    CACHE 1;
 2   DROP SEQUENCE public."PPMP_costcenterbudget_seq";
       public          postgres    false                        1259    20215    PPMP_ppmp_track_seq    SEQUENCE     ?   CREATE SEQUENCE public."PPMP_ppmp_track_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 99999999999
    CACHE 1;
 ,   DROP SEQUENCE public."PPMP_ppmp_track_seq";
       public          postgres    false            ?            1259    18068 
   auth_group    TABLE     f   CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);
    DROP TABLE public.auth_group;
       public         heap    eSmooothiee    false            ?            1259    18067    auth_group_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public          eSmooothiee    false    216            ?           0    0    auth_group_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;
          public          eSmooothiee    false    215            ?            1259    18077    auth_group_permissions    TABLE     ?   CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         heap    eSmooothiee    false            ?            1259    18076    auth_group_permissions_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public          eSmooothiee    false    218            ?           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;
          public          eSmooothiee    false    217            ?            1259    18061    auth_permission    TABLE     ?   CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         heap    eSmooothiee    false            ?            1259    18060    auth_permission_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public          eSmooothiee    false    214            ?           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;
          public          eSmooothiee    false    213            ?            1259    18084 	   auth_user    TABLE     ?  CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);
    DROP TABLE public.auth_user;
       public         heap    eSmooothiee    false            ?            1259    18093    auth_user_groups    TABLE     ~   CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);
 $   DROP TABLE public.auth_user_groups;
       public         heap    eSmooothiee    false            ?            1259    18092    auth_user_groups_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.auth_user_groups_id_seq;
       public          eSmooothiee    false    222                        0    0    auth_user_groups_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;
          public          eSmooothiee    false    221            ?            1259    18083    auth_user_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.auth_user_id_seq;
       public          eSmooothiee    false    220                       0    0    auth_user_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;
          public          eSmooothiee    false    219            ?            1259    18100    auth_user_user_permissions    TABLE     ?   CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);
 .   DROP TABLE public.auth_user_user_permissions;
       public         heap    eSmooothiee    false            ?            1259    18099 !   auth_user_user_permissions_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.auth_user_user_permissions_id_seq;
       public          eSmooothiee    false    224                       0    0 !   auth_user_user_permissions_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;
          public          eSmooothiee    false    223            ?            1259    19579    authtoken_token    TABLE     ?   CREATE TABLE public.authtoken_token (
    key character varying(40) NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);
 #   DROP TABLE public.authtoken_token;
       public         heap    eSmooothiee    false            ?            1259    18159    django_admin_log    TABLE     ?  CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public         heap    eSmooothiee    false            ?            1259    18158    django_admin_log_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public          eSmooothiee    false    226                       0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;
          public          eSmooothiee    false    225            ?            1259    18052    django_content_type    TABLE     ?   CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         heap    eSmooothiee    false            ?            1259    18051    django_content_type_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public          eSmooothiee    false    212                       0    0    django_content_type_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;
          public          eSmooothiee    false    211            ?            1259    18043    django_migrations    TABLE     ?   CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public         heap    eSmooothiee    false            ?            1259    18042    django_migrations_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public          eSmooothiee    false    210                       0    0    django_migrations_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;
          public          eSmooothiee    false    209            ?            1259    18188    django_session    TABLE     ?   CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         heap    eSmooothiee    false            ?            1259    18198    ppmp_app    TABLE     \  CREATE TABLE public.ppmp_app (
    id bigint NOT NULL,
    date_created timestamp with time zone NOT NULL,
    quarter character varying(255) NOT NULL,
    year character varying(255) NOT NULL,
    type character varying(255) NOT NULL,
    group_id character varying(255),
    item_desc_id bigint NOT NULL,
    source_of_fund_id bigint NOT NULL
);
    DROP TABLE public.ppmp_app;
       public         heap    eSmooothiee    false            ?            1259    18197    ppmp_app_id_seq    SEQUENCE     x   CREATE SEQUENCE public.ppmp_app_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.ppmp_app_id_seq;
       public          eSmooothiee    false    229                       0    0    ppmp_app_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.ppmp_app_id_seq OWNED BY public.ppmp_app.id;
          public          eSmooothiee    false    228            ?            1259    18207    ppmp_category    TABLE     ?   CREATE TABLE public.ppmp_category (
    id bigint NOT NULL,
    code character varying(255) NOT NULL,
    name character varying(255) NOT NULL
);
 !   DROP TABLE public.ppmp_category;
       public         heap    eSmooothiee    false            ?            1259    18206    ppmp_category_id_seq    SEQUENCE     }   CREATE SEQUENCE public.ppmp_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.ppmp_category_id_seq;
       public          eSmooothiee    false    231                       0    0    ppmp_category_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.ppmp_category_id_seq OWNED BY public.ppmp_category.id;
          public          eSmooothiee    false    230            ?            1259    18216    ppmp_costcenter    TABLE     ?   CREATE TABLE public.ppmp_costcenter (
    id bigint NOT NULL,
    code character varying(255) NOT NULL,
    name character varying(255) NOT NULL
);
 #   DROP TABLE public.ppmp_costcenter;
       public         heap    eSmooothiee    false            ?            1259    18215    ppmp_costcenter_id_seq    SEQUENCE        CREATE SEQUENCE public.ppmp_costcenter_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.ppmp_costcenter_id_seq;
       public          eSmooothiee    false    233                       0    0    ppmp_costcenter_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.ppmp_costcenter_id_seq OWNED BY public.ppmp_costcenter.id;
          public          eSmooothiee    false    232            ?            1259    18312    ppmp_costcenterbudget    TABLE     
  CREATE TABLE public.ppmp_costcenterbudget (
    id bigint NOT NULL,
    org_budget character varying(255) NOT NULL,
    category_id bigint NOT NULL,
    cc_id bigint NOT NULL,
    curr_budget character varying(255) NOT NULL,
    date_set timestamp with time zone
);
 )   DROP TABLE public.ppmp_costcenterbudget;
       public         heap    eSmooothiee    false            ?            1259    18311    ppmp_costcenterbudget_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.ppmp_costcenterbudget_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.ppmp_costcenterbudget_id_seq;
       public          eSmooothiee    false    253            	           0    0    ppmp_costcenterbudget_id_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.ppmp_costcenterbudget_id_seq OWNED BY public.ppmp_costcenterbudget.id;
          public          eSmooothiee    false    252            ?            1259    18305    ppmp_costcenteruser    TABLE     }   CREATE TABLE public.ppmp_costcenteruser (
    id bigint NOT NULL,
    cc_id bigint NOT NULL,
    user_id integer NOT NULL
);
 '   DROP TABLE public.ppmp_costcenteruser;
       public         heap    eSmooothiee    false            ?            1259    18304    ppmp_costcenteruser_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.ppmp_costcenteruser_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.ppmp_costcenteruser_id_seq;
       public          eSmooothiee    false    251            
           0    0    ppmp_costcenteruser_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.ppmp_costcenteruser_id_seq OWNED BY public.ppmp_costcenteruser.id;
          public          eSmooothiee    false    250            ?            1259    18225 	   ppmp_item    TABLE     ?   CREATE TABLE public.ppmp_item (
    id bigint NOT NULL,
    general_name character varying(255) NOT NULL,
    category_id bigint NOT NULL
);
    DROP TABLE public.ppmp_item;
       public         heap    eSmooothiee    false            ?            1259    18224    ppmp_item_id_seq    SEQUENCE     y   CREATE SEQUENCE public.ppmp_item_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.ppmp_item_id_seq;
       public          eSmooothiee    false    235                       0    0    ppmp_item_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.ppmp_item_id_seq OWNED BY public.ppmp_item.id;
          public          eSmooothiee    false    234            ?            1259    18232    ppmp_itemdescription    TABLE     >  CREATE TABLE public.ppmp_itemdescription (
    id bigint NOT NULL,
    spec_1 character varying(255) NOT NULL,
    item_id bigint NOT NULL,
    spec_2 character varying(255) NOT NULL,
    spec_3 character varying(255) NOT NULL,
    spec_4 character varying(255) NOT NULL,
    spec_5 character varying(255) NOT NULL
);
 (   DROP TABLE public.ppmp_itemdescription;
       public         heap    eSmooothiee    false            ?            1259    18231    ppmp_itemdescription_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.ppmp_itemdescription_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.ppmp_itemdescription_id_seq;
       public          eSmooothiee    false    237                       0    0    ppmp_itemdescription_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.ppmp_itemdescription_id_seq OWNED BY public.ppmp_itemdescription.id;
          public          eSmooothiee    false    236            ?            1259    18241    ppmp_orderdetails    TABLE     ?  CREATE TABLE public.ppmp_orderdetails (
    id bigint NOT NULL,
    app_status character varying(255),
    received_quotation_status character varying(255),
    award_winning_bidder_status character varying(255),
    obligate_po_status character varying(255),
    served_status character varying(255),
    qr_code character varying(255),
    first_quart_quant character varying(255),
    second_quart_quant character varying(255),
    fourth_quart_quant character varying(255),
    app_id bigint,
    item_desc_id bigint NOT NULL,
    ppmp_id bigint,
    price_id bigint,
    third_quart_quant character varying(255),
    date character varying(255)
);
 %   DROP TABLE public.ppmp_orderdetails;
       public         heap    eSmooothiee    false            ?            1259    18240    ppmp_orderdetails_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.ppmp_orderdetails_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.ppmp_orderdetails_id_seq;
       public          eSmooothiee    false    239                       0    0    ppmp_orderdetails_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.ppmp_orderdetails_id_seq OWNED BY public.ppmp_orderdetails.id;
          public          eSmooothiee    false    238            ?            1259    18286 	   ppmp_ppmp    TABLE       CREATE TABLE public.ppmp_ppmp (
    id bigint NOT NULL,
    year character varying(255) NOT NULL,
    type character varying(255) NOT NULL,
    cc_id bigint NOT NULL,
    sof_id bigint NOT NULL,
    is_lock boolean NOT NULL,
    is_deleted boolean NOT NULL
);
    DROP TABLE public.ppmp_ppmp;
       public         heap    eSmooothiee    false            ?            1259    18285    ppmp_ppmp_id_seq    SEQUENCE     y   CREATE SEQUENCE public.ppmp_ppmp_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.ppmp_ppmp_id_seq;
       public          eSmooothiee    false    249                       0    0    ppmp_ppmp_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.ppmp_ppmp_id_seq OWNED BY public.ppmp_ppmp.id;
          public          eSmooothiee    false    248                       1259    20477    ppmp_ppmp_key_log    TABLE     ?   CREATE TABLE public.ppmp_ppmp_key_log (
    id bigint NOT NULL,
    datetime timestamp with time zone NOT NULL,
    is_lock boolean NOT NULL,
    ppmp_id bigint NOT NULL,
    user_id integer NOT NULL
);
 %   DROP TABLE public.ppmp_ppmp_key_log;
       public         heap    eSmooothiee    false                       1259    20476    ppmp_ppmp_key_log_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.ppmp_ppmp_key_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.ppmp_ppmp_key_log_id_seq;
       public          eSmooothiee    false    258                       0    0    ppmp_ppmp_key_log_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.ppmp_ppmp_key_log_id_seq OWNED BY public.ppmp_ppmp_key_log.id;
          public          eSmooothiee    false    257            ?            1259    18250    ppmp_ppmptrack    TABLE     ?   CREATE TABLE public.ppmp_ppmptrack (
    id bigint NOT NULL,
    datetime character varying(255),
    cc_name character varying(255),
    barcode character varying(255),
    orderdetails_id bigint
);
 "   DROP TABLE public.ppmp_ppmptrack;
       public         heap    eSmooothiee    false            ?            1259    18249    ppmp_ppmptrack_id_seq    SEQUENCE     ~   CREATE SEQUENCE public.ppmp_ppmptrack_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.ppmp_ppmptrack_id_seq;
       public          eSmooothiee    false    241                       0    0    ppmp_ppmptrack_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.ppmp_ppmptrack_id_seq OWNED BY public.ppmp_ppmptrack.id;
          public          eSmooothiee    false    240            ?            1259    18277    ppmp_prices    TABLE     ?   CREATE TABLE public.ppmp_prices (
    id bigint NOT NULL,
    price character varying(255) NOT NULL,
    date_created timestamp with time zone NOT NULL,
    unit character varying(255) NOT NULL,
    item_id bigint NOT NULL
);
    DROP TABLE public.ppmp_prices;
       public         heap    eSmooothiee    false            ?            1259    18276    ppmp_prices_id_seq    SEQUENCE     {   CREATE SEQUENCE public.ppmp_prices_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.ppmp_prices_id_seq;
       public          eSmooothiee    false    247                       0    0    ppmp_prices_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.ppmp_prices_id_seq OWNED BY public.ppmp_prices.id;
          public          eSmooothiee    false    246            ?            1259    18268    ppmp_purchaserequest    TABLE       CREATE TABLE public.ppmp_purchaserequest (
    id bigint NOT NULL,
    specification_details character varying(255) NOT NULL,
    purpose character varying(255) NOT NULL,
    date_created timestamp with time zone NOT NULL,
    order_details_id bigint NOT NULL
);
 (   DROP TABLE public.ppmp_purchaserequest;
       public         heap    eSmooothiee    false            ?            1259    18267    ppmp_purchaserequest_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.ppmp_purchaserequest_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.ppmp_purchaserequest_id_seq;
       public          eSmooothiee    false    245                       0    0    ppmp_purchaserequest_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.ppmp_purchaserequest_id_seq OWNED BY public.ppmp_purchaserequest.id;
          public          eSmooothiee    false    244            ?            1259    18259    ppmp_sourceoffund    TABLE     ?   CREATE TABLE public.ppmp_sourceoffund (
    id bigint NOT NULL,
    code character varying(255) NOT NULL,
    description character varying(255) NOT NULL
);
 %   DROP TABLE public.ppmp_sourceoffund;
       public         heap    eSmooothiee    false            ?            1259    18258    ppmp_sourceoffund_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.ppmp_sourceoffund_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.ppmp_sourceoffund_id_seq;
       public          eSmooothiee    false    243                       0    0    ppmp_sourceoffund_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.ppmp_sourceoffund_id_seq OWNED BY public.ppmp_sourceoffund.id;
          public          eSmooothiee    false    242            ?           2604    18071    auth_group id    DEFAULT     n   ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public          eSmooothiee    false    215    216    216            ?           2604    18080    auth_group_permissions id    DEFAULT     ?   ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public          eSmooothiee    false    218    217    218            ?           2604    18064    auth_permission id    DEFAULT     x   ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public          eSmooothiee    false    213    214    214            ?           2604    18087    auth_user id    DEFAULT     l   ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);
 ;   ALTER TABLE public.auth_user ALTER COLUMN id DROP DEFAULT;
       public          eSmooothiee    false    220    219    220            ?           2604    18096    auth_user_groups id    DEFAULT     z   ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);
 B   ALTER TABLE public.auth_user_groups ALTER COLUMN id DROP DEFAULT;
       public          eSmooothiee    false    222    221    222            ?           2604    18103    auth_user_user_permissions id    DEFAULT     ?   ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);
 L   ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id DROP DEFAULT;
       public          eSmooothiee    false    224    223    224            ?           2604    18162    django_admin_log id    DEFAULT     z   ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public          eSmooothiee    false    226    225    226            ?           2604    18055    django_content_type id    DEFAULT     ?   ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public          eSmooothiee    false    211    212    212            ?           2604    18046    django_migrations id    DEFAULT     |   ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public          eSmooothiee    false    209    210    210            ?           2604    18201    ppmp_app id    DEFAULT     j   ALTER TABLE ONLY public.ppmp_app ALTER COLUMN id SET DEFAULT nextval('public.ppmp_app_id_seq'::regclass);
 :   ALTER TABLE public.ppmp_app ALTER COLUMN id DROP DEFAULT;
       public          eSmooothiee    false    229    228    229            ?           2604    18210    ppmp_category id    DEFAULT     t   ALTER TABLE ONLY public.ppmp_category ALTER COLUMN id SET DEFAULT nextval('public.ppmp_category_id_seq'::regclass);
 ?   ALTER TABLE public.ppmp_category ALTER COLUMN id DROP DEFAULT;
       public          eSmooothiee    false    230    231    231            ?           2604    18219    ppmp_costcenter id    DEFAULT     x   ALTER TABLE ONLY public.ppmp_costcenter ALTER COLUMN id SET DEFAULT nextval('public.ppmp_costcenter_id_seq'::regclass);
 A   ALTER TABLE public.ppmp_costcenter ALTER COLUMN id DROP DEFAULT;
       public          eSmooothiee    false    233    232    233            ?           2604    18315    ppmp_costcenterbudget id    DEFAULT     ?   ALTER TABLE ONLY public.ppmp_costcenterbudget ALTER COLUMN id SET DEFAULT nextval('public.ppmp_costcenterbudget_id_seq'::regclass);
 G   ALTER TABLE public.ppmp_costcenterbudget ALTER COLUMN id DROP DEFAULT;
       public          eSmooothiee    false    253    252    253            ?           2604    18308    ppmp_costcenteruser id    DEFAULT     ?   ALTER TABLE ONLY public.ppmp_costcenteruser ALTER COLUMN id SET DEFAULT nextval('public.ppmp_costcenteruser_id_seq'::regclass);
 E   ALTER TABLE public.ppmp_costcenteruser ALTER COLUMN id DROP DEFAULT;
       public          eSmooothiee    false    250    251    251            ?           2604    18228    ppmp_item id    DEFAULT     l   ALTER TABLE ONLY public.ppmp_item ALTER COLUMN id SET DEFAULT nextval('public.ppmp_item_id_seq'::regclass);
 ;   ALTER TABLE public.ppmp_item ALTER COLUMN id DROP DEFAULT;
       public          eSmooothiee    false    234    235    235            ?           2604    18235    ppmp_itemdescription id    DEFAULT     ?   ALTER TABLE ONLY public.ppmp_itemdescription ALTER COLUMN id SET DEFAULT nextval('public.ppmp_itemdescription_id_seq'::regclass);
 F   ALTER TABLE public.ppmp_itemdescription ALTER COLUMN id DROP DEFAULT;
       public          eSmooothiee    false    236    237    237            ?           2604    18244    ppmp_orderdetails id    DEFAULT     |   ALTER TABLE ONLY public.ppmp_orderdetails ALTER COLUMN id SET DEFAULT nextval('public.ppmp_orderdetails_id_seq'::regclass);
 C   ALTER TABLE public.ppmp_orderdetails ALTER COLUMN id DROP DEFAULT;
       public          eSmooothiee    false    239    238    239            ?           2604    18289    ppmp_ppmp id    DEFAULT     l   ALTER TABLE ONLY public.ppmp_ppmp ALTER COLUMN id SET DEFAULT nextval('public.ppmp_ppmp_id_seq'::regclass);
 ;   ALTER TABLE public.ppmp_ppmp ALTER COLUMN id DROP DEFAULT;
       public          eSmooothiee    false    249    248    249            ?           2604    20480    ppmp_ppmp_key_log id    DEFAULT     |   ALTER TABLE ONLY public.ppmp_ppmp_key_log ALTER COLUMN id SET DEFAULT nextval('public.ppmp_ppmp_key_log_id_seq'::regclass);
 C   ALTER TABLE public.ppmp_ppmp_key_log ALTER COLUMN id DROP DEFAULT;
       public          eSmooothiee    false    258    257    258            ?           2604    18253    ppmp_ppmptrack id    DEFAULT     v   ALTER TABLE ONLY public.ppmp_ppmptrack ALTER COLUMN id SET DEFAULT nextval('public.ppmp_ppmptrack_id_seq'::regclass);
 @   ALTER TABLE public.ppmp_ppmptrack ALTER COLUMN id DROP DEFAULT;
       public          eSmooothiee    false    240    241    241            ?           2604    18280    ppmp_prices id    DEFAULT     p   ALTER TABLE ONLY public.ppmp_prices ALTER COLUMN id SET DEFAULT nextval('public.ppmp_prices_id_seq'::regclass);
 =   ALTER TABLE public.ppmp_prices ALTER COLUMN id DROP DEFAULT;
       public          eSmooothiee    false    247    246    247            ?           2604    18271    ppmp_purchaserequest id    DEFAULT     ?   ALTER TABLE ONLY public.ppmp_purchaserequest ALTER COLUMN id SET DEFAULT nextval('public.ppmp_purchaserequest_id_seq'::regclass);
 F   ALTER TABLE public.ppmp_purchaserequest ALTER COLUMN id DROP DEFAULT;
       public          eSmooothiee    false    244    245    245            ?           2604    18262    ppmp_sourceoffund id    DEFAULT     |   ALTER TABLE ONLY public.ppmp_sourceoffund ALTER COLUMN id SET DEFAULT nextval('public.ppmp_sourceoffund_id_seq'::regclass);
 C   ALTER TABLE public.ppmp_sourceoffund ALTER COLUMN id DROP DEFAULT;
       public          eSmooothiee    false    242    243    243            ?           2606    18186    auth_group auth_group_name_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public            eSmooothiee    false    216            ?           2606    18116 R   auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   CONSTRAINT     ?   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);
 |   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
       public            eSmooothiee    false    218    218                       2606    18082 2   auth_group_permissions auth_group_permissions_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public            eSmooothiee    false    218            ?           2606    18073    auth_group auth_group_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public            eSmooothiee    false    216            ?           2606    18107 F   auth_permission auth_permission_content_type_id_codename_01ab375a_uniq 
   CONSTRAINT     ?   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);
 p   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
       public            eSmooothiee    false    214    214            ?           2606    18066 $   auth_permission auth_permission_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public            eSmooothiee    false    214            	           2606    18098 &   auth_user_groups auth_user_groups_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
       public            eSmooothiee    false    222                       2606    18131 @   auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq 
   CONSTRAINT     ?   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);
 j   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq;
       public            eSmooothiee    false    222    222                       2606    18089    auth_user auth_user_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
       public            eSmooothiee    false    220                       2606    18105 :   auth_user_user_permissions auth_user_user_permissions_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);
 d   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
       public            eSmooothiee    false    224                       2606    18145 Y   auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq 
   CONSTRAINT     ?   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);
 ?   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq;
       public            eSmooothiee    false    224    224                       2606    18181     auth_user auth_user_username_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);
 J   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
       public            eSmooothiee    false    220            H           2606    19583 $   authtoken_token authtoken_token_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_pkey PRIMARY KEY (key);
 N   ALTER TABLE ONLY public.authtoken_token DROP CONSTRAINT authtoken_token_pkey;
       public            eSmooothiee    false    254            J           2606    19585 +   authtoken_token authtoken_token_user_id_key 
   CONSTRAINT     i   ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id);
 U   ALTER TABLE ONLY public.authtoken_token DROP CONSTRAINT authtoken_token_user_id_key;
       public            eSmooothiee    false    254                       2606    18167 &   django_admin_log django_admin_log_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public            eSmooothiee    false    226            ?           2606    18059 E   django_content_type django_content_type_app_label_model_76bd3d3b_uniq 
   CONSTRAINT     ?   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);
 o   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
       public            eSmooothiee    false    212    212            ?           2606    18057 ,   django_content_type django_content_type_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public            eSmooothiee    false    212            ?           2606    18050 (   django_migrations django_migrations_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public            eSmooothiee    false    210                       2606    18194 "   django_session django_session_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public            eSmooothiee    false    227                       2606    18205    ppmp_app ppmp_app_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.ppmp_app
    ADD CONSTRAINT ppmp_app_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.ppmp_app DROP CONSTRAINT ppmp_app_pkey;
       public            eSmooothiee    false    229                        2606    18214     ppmp_category ppmp_category_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.ppmp_category
    ADD CONSTRAINT ppmp_category_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.ppmp_category DROP CONSTRAINT ppmp_category_pkey;
       public            eSmooothiee    false    231            "           2606    18223 $   ppmp_costcenter ppmp_costcenter_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.ppmp_costcenter
    ADD CONSTRAINT ppmp_costcenter_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.ppmp_costcenter DROP CONSTRAINT ppmp_costcenter_pkey;
       public            eSmooothiee    false    233            E           2606    18317 0   ppmp_costcenterbudget ppmp_costcenterbudget_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.ppmp_costcenterbudget
    ADD CONSTRAINT ppmp_costcenterbudget_pkey PRIMARY KEY (id);
 Z   ALTER TABLE ONLY public.ppmp_costcenterbudget DROP CONSTRAINT ppmp_costcenterbudget_pkey;
       public            eSmooothiee    false    253            @           2606    18310 ,   ppmp_costcenteruser ppmp_costcenteruser_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.ppmp_costcenteruser
    ADD CONSTRAINT ppmp_costcenteruser_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.ppmp_costcenteruser DROP CONSTRAINT ppmp_costcenteruser_pkey;
       public            eSmooothiee    false    251            %           2606    18230    ppmp_item ppmp_item_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.ppmp_item
    ADD CONSTRAINT ppmp_item_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.ppmp_item DROP CONSTRAINT ppmp_item_pkey;
       public            eSmooothiee    false    235            (           2606    18239 .   ppmp_itemdescription ppmp_itemdescription_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.ppmp_itemdescription
    ADD CONSTRAINT ppmp_itemdescription_pkey PRIMARY KEY (id);
 X   ALTER TABLE ONLY public.ppmp_itemdescription DROP CONSTRAINT ppmp_itemdescription_pkey;
       public            eSmooothiee    false    237            ,           2606    18248 (   ppmp_orderdetails ppmp_orderdetails_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.ppmp_orderdetails
    ADD CONSTRAINT ppmp_orderdetails_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.ppmp_orderdetails DROP CONSTRAINT ppmp_orderdetails_pkey;
       public            eSmooothiee    false    239            L           2606    20482 (   ppmp_ppmp_key_log ppmp_ppmp_key_log_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.ppmp_ppmp_key_log
    ADD CONSTRAINT ppmp_ppmp_key_log_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.ppmp_ppmp_key_log DROP CONSTRAINT ppmp_ppmp_key_log_pkey;
       public            eSmooothiee    false    258            <           2606    18293    ppmp_ppmp ppmp_ppmp_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.ppmp_ppmp
    ADD CONSTRAINT ppmp_ppmp_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.ppmp_ppmp DROP CONSTRAINT ppmp_ppmp_pkey;
       public            eSmooothiee    false    249            1           2606    18257 "   ppmp_ppmptrack ppmp_ppmptrack_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.ppmp_ppmptrack
    ADD CONSTRAINT ppmp_ppmptrack_pkey PRIMARY KEY (id);
 L   ALTER TABLE ONLY public.ppmp_ppmptrack DROP CONSTRAINT ppmp_ppmptrack_pkey;
       public            eSmooothiee    false    241            9           2606    18284    ppmp_prices ppmp_prices_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.ppmp_prices
    ADD CONSTRAINT ppmp_prices_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.ppmp_prices DROP CONSTRAINT ppmp_prices_pkey;
       public            eSmooothiee    false    247            6           2606    18275 .   ppmp_purchaserequest ppmp_purchaserequest_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.ppmp_purchaserequest
    ADD CONSTRAINT ppmp_purchaserequest_pkey PRIMARY KEY (id);
 X   ALTER TABLE ONLY public.ppmp_purchaserequest DROP CONSTRAINT ppmp_purchaserequest_pkey;
       public            eSmooothiee    false    245            3           2606    18266 (   ppmp_sourceoffund ppmp_sourceoffund_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.ppmp_sourceoffund
    ADD CONSTRAINT ppmp_sourceoffund_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.ppmp_sourceoffund DROP CONSTRAINT ppmp_sourceoffund_pkey;
       public            eSmooothiee    false    243            ?           1259    18187    auth_group_name_a6ea08ec_like    INDEX     h   CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);
 1   DROP INDEX public.auth_group_name_a6ea08ec_like;
       public            eSmooothiee    false    216            ?           1259    18127 (   auth_group_permissions_group_id_b120cbf9    INDEX     o   CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
 <   DROP INDEX public.auth_group_permissions_group_id_b120cbf9;
       public            eSmooothiee    false    218            ?           1259    18128 -   auth_group_permissions_permission_id_84c5c92e    INDEX     y   CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);
 A   DROP INDEX public.auth_group_permissions_permission_id_84c5c92e;
       public            eSmooothiee    false    218            ?           1259    18113 (   auth_permission_content_type_id_2f476e4b    INDEX     o   CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);
 <   DROP INDEX public.auth_permission_content_type_id_2f476e4b;
       public            eSmooothiee    false    214                       1259    18143 "   auth_user_groups_group_id_97559544    INDEX     c   CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);
 6   DROP INDEX public.auth_user_groups_group_id_97559544;
       public            eSmooothiee    false    222            
           1259    18142 !   auth_user_groups_user_id_6a12ed8b    INDEX     a   CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);
 5   DROP INDEX public.auth_user_groups_user_id_6a12ed8b;
       public            eSmooothiee    false    222                       1259    18157 1   auth_user_user_permissions_permission_id_1fbb5f2c    INDEX     ?   CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);
 E   DROP INDEX public.auth_user_user_permissions_permission_id_1fbb5f2c;
       public            eSmooothiee    false    224                       1259    18156 +   auth_user_user_permissions_user_id_a95ead1b    INDEX     u   CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);
 ?   DROP INDEX public.auth_user_user_permissions_user_id_a95ead1b;
       public            eSmooothiee    false    224                       1259    18182     auth_user_username_6821ab7c_like    INDEX     n   CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);
 4   DROP INDEX public.auth_user_username_6821ab7c_like;
       public            eSmooothiee    false    220            F           1259    19591 !   authtoken_token_key_10f0b77e_like    INDEX     p   CREATE INDEX authtoken_token_key_10f0b77e_like ON public.authtoken_token USING btree (key varchar_pattern_ops);
 5   DROP INDEX public.authtoken_token_key_10f0b77e_like;
       public            eSmooothiee    false    254                       1259    18178 )   django_admin_log_content_type_id_c4bce8eb    INDEX     q   CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
 =   DROP INDEX public.django_admin_log_content_type_id_c4bce8eb;
       public            eSmooothiee    false    226                       1259    18179 !   django_admin_log_user_id_c564eba6    INDEX     a   CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);
 5   DROP INDEX public.django_admin_log_user_id_c564eba6;
       public            eSmooothiee    false    226                       1259    18196 #   django_session_expire_date_a5c62663    INDEX     e   CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
 7   DROP INDEX public.django_session_expire_date_a5c62663;
       public            eSmooothiee    false    227                       1259    18195 (   django_session_session_key_c0390e0f_like    INDEX     ~   CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);
 <   DROP INDEX public.django_session_session_key_c0390e0f_like;
       public            eSmooothiee    false    227                       1259    18402 !   ppmp_app_item_desc_id_id_6f1584ba    INDEX     ^   CREATE INDEX ppmp_app_item_desc_id_id_6f1584ba ON public.ppmp_app USING btree (item_desc_id);
 5   DROP INDEX public.ppmp_app_item_desc_id_id_6f1584ba;
       public            eSmooothiee    false    229                       1259    18403 &   ppmp_app_source_of_fund_id_id_7ed302de    INDEX     h   CREATE INDEX ppmp_app_source_of_fund_id_id_7ed302de ON public.ppmp_app USING btree (source_of_fund_id);
 :   DROP INDEX public.ppmp_app_source_of_fund_id_id_7ed302de;
       public            eSmooothiee    false    229            B           1259    18400 (   ppmp_costcenterbudget_cat_id_id_398001f3    INDEX     q   CREATE INDEX ppmp_costcenterbudget_cat_id_id_398001f3 ON public.ppmp_costcenterbudget USING btree (category_id);
 <   DROP INDEX public.ppmp_costcenterbudget_cat_id_id_398001f3;
       public            eSmooothiee    false    253            C           1259    18401 '   ppmp_costcenterbudget_cc_id_id_7951a2a8    INDEX     j   CREATE INDEX ppmp_costcenterbudget_cc_id_id_7951a2a8 ON public.ppmp_costcenterbudget USING btree (cc_id);
 ;   DROP INDEX public.ppmp_costcenterbudget_cc_id_id_7951a2a8;
       public            eSmooothiee    false    253            >           1259    18388 %   ppmp_costcenteruser_cc_id_id_b09e33fb    INDEX     f   CREATE INDEX ppmp_costcenteruser_cc_id_id_b09e33fb ON public.ppmp_costcenteruser USING btree (cc_id);
 9   DROP INDEX public.ppmp_costcenteruser_cc_id_id_b09e33fb;
       public            eSmooothiee    false    251            A           1259    18389 '   ppmp_costcenteruser_user_id_id_01bb5ec8    INDEX     j   CREATE INDEX ppmp_costcenteruser_user_id_id_01bb5ec8 ON public.ppmp_costcenteruser USING btree (user_id);
 ;   DROP INDEX public.ppmp_costcenteruser_user_id_id_01bb5ec8;
       public            eSmooothiee    false    251            #           1259    18333    ppmp_item_cat_id_id_0fe98e34    INDEX     Y   CREATE INDEX ppmp_item_cat_id_id_0fe98e34 ON public.ppmp_item USING btree (category_id);
 0   DROP INDEX public.ppmp_item_cat_id_id_0fe98e34;
       public            eSmooothiee    false    235            &           1259    18339 (   ppmp_itemdescription_item_id_id_8e0c1f8d    INDEX     l   CREATE INDEX ppmp_itemdescription_item_id_id_8e0c1f8d ON public.ppmp_itemdescription USING btree (item_id);
 <   DROP INDEX public.ppmp_itemdescription_item_id_id_8e0c1f8d;
       public            eSmooothiee    false    237            )           1259    18350 $   ppmp_orderdetails_app_id_id_2f33dfde    INDEX     d   CREATE INDEX ppmp_orderdetails_app_id_id_2f33dfde ON public.ppmp_orderdetails USING btree (app_id);
 8   DROP INDEX public.ppmp_orderdetails_app_id_id_2f33dfde;
       public            eSmooothiee    false    239            *           1259    18351 *   ppmp_orderdetails_item_desc_id_id_024c0c35    INDEX     p   CREATE INDEX ppmp_orderdetails_item_desc_id_id_024c0c35 ON public.ppmp_orderdetails USING btree (item_desc_id);
 >   DROP INDEX public.ppmp_orderdetails_item_desc_id_id_024c0c35;
       public            eSmooothiee    false    239            -           1259    18376 %   ppmp_orderdetails_ppmp_id_id_025c676c    INDEX     f   CREATE INDEX ppmp_orderdetails_ppmp_id_id_025c676c ON public.ppmp_orderdetails USING btree (ppmp_id);
 9   DROP INDEX public.ppmp_orderdetails_ppmp_id_id_025c676c;
       public            eSmooothiee    false    239            .           1259    18377 &   ppmp_orderdetails_price_id_id_1ba7d544    INDEX     h   CREATE INDEX ppmp_orderdetails_price_id_id_1ba7d544 ON public.ppmp_orderdetails USING btree (price_id);
 :   DROP INDEX public.ppmp_orderdetails_price_id_id_1ba7d544;
       public            eSmooothiee    false    239            :           1259    18374    ppmp_ppmp_cc_num_id_id_dfbd0001    INDEX     V   CREATE INDEX ppmp_ppmp_cc_num_id_id_dfbd0001 ON public.ppmp_ppmp USING btree (cc_id);
 3   DROP INDEX public.ppmp_ppmp_cc_num_id_id_dfbd0001;
       public            eSmooothiee    false    249            M           1259    20493 "   ppmp_ppmp_key_log_ppmp_id_47ee7be0    INDEX     c   CREATE INDEX ppmp_ppmp_key_log_ppmp_id_47ee7be0 ON public.ppmp_ppmp_key_log USING btree (ppmp_id);
 6   DROP INDEX public.ppmp_ppmp_key_log_ppmp_id_47ee7be0;
       public            eSmooothiee    false    258            N           1259    20494 "   ppmp_ppmp_key_log_user_id_2ef306ff    INDEX     c   CREATE INDEX ppmp_ppmp_key_log_user_id_2ef306ff ON public.ppmp_ppmp_key_log USING btree (user_id);
 6   DROP INDEX public.ppmp_ppmp_key_log_user_id_2ef306ff;
       public            eSmooothiee    false    258            =           1259    18375     ppmp_ppmp_sof_num_id_id_837ad153    INDEX     X   CREATE INDEX ppmp_ppmp_sof_num_id_id_837ad153 ON public.ppmp_ppmp USING btree (sof_id);
 4   DROP INDEX public.ppmp_ppmp_sof_num_id_id_837ad153;
       public            eSmooothiee    false    249            /           1259    20465 '   ppmp_ppmptrack_orderdetails_id_2ac018eb    INDEX     m   CREATE INDEX ppmp_ppmptrack_orderdetails_id_2ac018eb ON public.ppmp_ppmptrack USING btree (orderdetails_id);
 ;   DROP INDEX public.ppmp_ppmptrack_orderdetails_id_2ac018eb;
       public            eSmooothiee    false    241            7           1259    18363    ppmp_prices_item_id_id_41d9554f    INDEX     Z   CREATE INDEX ppmp_prices_item_id_id_41d9554f ON public.ppmp_prices USING btree (item_id);
 3   DROP INDEX public.ppmp_prices_item_id_id_41d9554f;
       public            eSmooothiee    false    247            4           1259    18357 1   ppmp_purchaserequest_order_details_id_id_d237ad89    INDEX     ~   CREATE INDEX ppmp_purchaserequest_order_details_id_id_d237ad89 ON public.ppmp_purchaserequest USING btree (order_details_id);
 E   DROP INDEX public.ppmp_purchaserequest_order_details_id_id_d237ad89;
       public            eSmooothiee    false    245            Q           2606    18122 O   auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm    FK CONSTRAINT     ?   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
       public          eSmooothiee    false    214    3318    218            P           2606    18117 P   auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
       public          eSmooothiee    false    216    218    3323            O           2606    18108 E   auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co    FK CONSTRAINT     ?   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
       public          eSmooothiee    false    212    214    3313            S           2606    18137 D   auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id;
       public          eSmooothiee    false    222    3323    216            R           2606    18132 B   auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id;
       public          eSmooothiee    false    220    222    3331            U           2606    18151 S   auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm    FK CONSTRAINT     ?   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 }   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm;
       public          eSmooothiee    false    224    214    3318            T           2606    18146 V   auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 ?   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id;
       public          eSmooothiee    false    220    224    3331            i           2606    19586 @   authtoken_token authtoken_token_user_id_35299eff_fk_auth_user_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_35299eff_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 j   ALTER TABLE ONLY public.authtoken_token DROP CONSTRAINT authtoken_token_user_id_35299eff_fk_auth_user_id;
       public          eSmooothiee    false    3331    220    254            V           2606    18168 G   django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co    FK CONSTRAINT     ?   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co;
       public          eSmooothiee    false    226    212    3313            W           2606    18173 B   django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id;
       public          eSmooothiee    false    3331    226    220            X           2606    18405 B   ppmp_app ppmp_app_item_desc_id_764e010d_fk_ppmp_itemdescription_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ppmp_app
    ADD CONSTRAINT ppmp_app_item_desc_id_764e010d_fk_ppmp_itemdescription_id FOREIGN KEY (item_desc_id) REFERENCES public.ppmp_itemdescription(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.ppmp_app DROP CONSTRAINT ppmp_app_item_desc_id_764e010d_fk_ppmp_itemdescription_id;
       public          eSmooothiee    false    237    3368    229            Y           2606    18410 D   ppmp_app ppmp_app_source_of_fund_id_71aee7b1_fk_ppmp_sourceoffund_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ppmp_app
    ADD CONSTRAINT ppmp_app_source_of_fund_id_71aee7b1_fk_ppmp_sourceoffund_id FOREIGN KEY (source_of_fund_id) REFERENCES public.ppmp_sourceoffund(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.ppmp_app DROP CONSTRAINT ppmp_app_source_of_fund_id_71aee7b1_fk_ppmp_sourceoffund_id;
       public          eSmooothiee    false    3379    243    229            g           2606    18415 T   ppmp_costcenterbudget ppmp_costcenterbudget_category_id_07774e3a_fk_ppmp_category_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ppmp_costcenterbudget
    ADD CONSTRAINT ppmp_costcenterbudget_category_id_07774e3a_fk_ppmp_category_id FOREIGN KEY (category_id) REFERENCES public.ppmp_category(id) DEFERRABLE INITIALLY DEFERRED;
 ~   ALTER TABLE ONLY public.ppmp_costcenterbudget DROP CONSTRAINT ppmp_costcenterbudget_category_id_07774e3a_fk_ppmp_category_id;
       public          eSmooothiee    false    231    253    3360            h           2606    18420 P   ppmp_costcenterbudget ppmp_costcenterbudget_cc_id_023e533c_fk_ppmp_costcenter_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ppmp_costcenterbudget
    ADD CONSTRAINT ppmp_costcenterbudget_cc_id_023e533c_fk_ppmp_costcenter_id FOREIGN KEY (cc_id) REFERENCES public.ppmp_costcenter(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.ppmp_costcenterbudget DROP CONSTRAINT ppmp_costcenterbudget_cc_id_023e533c_fk_ppmp_costcenter_id;
       public          eSmooothiee    false    3362    253    233            e           2606    18425 L   ppmp_costcenteruser ppmp_costcenteruser_cc_id_b37aa280_fk_ppmp_costcenter_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ppmp_costcenteruser
    ADD CONSTRAINT ppmp_costcenteruser_cc_id_b37aa280_fk_ppmp_costcenter_id FOREIGN KEY (cc_id) REFERENCES public.ppmp_costcenter(id) DEFERRABLE INITIALLY DEFERRED;
 v   ALTER TABLE ONLY public.ppmp_costcenteruser DROP CONSTRAINT ppmp_costcenteruser_cc_id_b37aa280_fk_ppmp_costcenter_id;
       public          eSmooothiee    false    233    3362    251            f           2606    18430 H   ppmp_costcenteruser ppmp_costcenteruser_user_id_26b70148_fk_auth_user_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ppmp_costcenteruser
    ADD CONSTRAINT ppmp_costcenteruser_user_id_26b70148_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 r   ALTER TABLE ONLY public.ppmp_costcenteruser DROP CONSTRAINT ppmp_costcenteruser_user_id_26b70148_fk_auth_user_id;
       public          eSmooothiee    false    3331    220    251            Z           2606    18435 <   ppmp_item ppmp_item_category_id_76338be4_fk_ppmp_category_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ppmp_item
    ADD CONSTRAINT ppmp_item_category_id_76338be4_fk_ppmp_category_id FOREIGN KEY (category_id) REFERENCES public.ppmp_category(id) DEFERRABLE INITIALLY DEFERRED;
 f   ALTER TABLE ONLY public.ppmp_item DROP CONSTRAINT ppmp_item_category_id_76338be4_fk_ppmp_category_id;
       public          eSmooothiee    false    3360    231    235            [           2606    18440 J   ppmp_itemdescription ppmp_itemdescription_item_id_a1cd441c_fk_ppmp_item_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ppmp_itemdescription
    ADD CONSTRAINT ppmp_itemdescription_item_id_a1cd441c_fk_ppmp_item_id FOREIGN KEY (item_id) REFERENCES public.ppmp_item(id) DEFERRABLE INITIALLY DEFERRED;
 t   ALTER TABLE ONLY public.ppmp_itemdescription DROP CONSTRAINT ppmp_itemdescription_item_id_a1cd441c_fk_ppmp_item_id;
       public          eSmooothiee    false    237    3365    235            ]           2606    20435 B   ppmp_orderdetails ppmp_orderdetails_app_id_bcd6c834_fk_ppmp_app_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ppmp_orderdetails
    ADD CONSTRAINT ppmp_orderdetails_app_id_bcd6c834_fk_ppmp_app_id FOREIGN KEY (app_id) REFERENCES public.ppmp_app(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.ppmp_orderdetails DROP CONSTRAINT ppmp_orderdetails_app_id_bcd6c834_fk_ppmp_app_id;
       public          eSmooothiee    false    239    229    3357            \           2606    18450 F   ppmp_orderdetails ppmp_orderdetails_item_desc_id_f9185c6d_fk_ppmp_item    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ppmp_orderdetails
    ADD CONSTRAINT ppmp_orderdetails_item_desc_id_f9185c6d_fk_ppmp_item FOREIGN KEY (item_desc_id) REFERENCES public.ppmp_itemdescription(id) DEFERRABLE INITIALLY DEFERRED;
 p   ALTER TABLE ONLY public.ppmp_orderdetails DROP CONSTRAINT ppmp_orderdetails_item_desc_id_f9185c6d_fk_ppmp_item;
       public          eSmooothiee    false    237    239    3368            ^           2606    20440 D   ppmp_orderdetails ppmp_orderdetails_ppmp_id_5179df2e_fk_ppmp_ppmp_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ppmp_orderdetails
    ADD CONSTRAINT ppmp_orderdetails_ppmp_id_5179df2e_fk_ppmp_ppmp_id FOREIGN KEY (ppmp_id) REFERENCES public.ppmp_ppmp(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.ppmp_orderdetails DROP CONSTRAINT ppmp_orderdetails_ppmp_id_5179df2e_fk_ppmp_ppmp_id;
       public          eSmooothiee    false    239    249    3388            _           2606    20445 G   ppmp_orderdetails ppmp_orderdetails_price_id_b7d6dffb_fk_ppmp_prices_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ppmp_orderdetails
    ADD CONSTRAINT ppmp_orderdetails_price_id_b7d6dffb_fk_ppmp_prices_id FOREIGN KEY (price_id) REFERENCES public.ppmp_prices(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.ppmp_orderdetails DROP CONSTRAINT ppmp_orderdetails_price_id_b7d6dffb_fk_ppmp_prices_id;
       public          eSmooothiee    false    3385    247    239            c           2606    19569 8   ppmp_ppmp ppmp_ppmp_cc_id_dc8ff97d_fk_ppmp_costcenter_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ppmp_ppmp
    ADD CONSTRAINT ppmp_ppmp_cc_id_dc8ff97d_fk_ppmp_costcenter_id FOREIGN KEY (cc_id) REFERENCES public.ppmp_costcenter(id) DEFERRABLE INITIALLY DEFERRED;
 b   ALTER TABLE ONLY public.ppmp_ppmp DROP CONSTRAINT ppmp_ppmp_cc_id_dc8ff97d_fk_ppmp_costcenter_id;
       public          eSmooothiee    false    233    3362    249            j           2606    20483 D   ppmp_ppmp_key_log ppmp_ppmp_key_log_ppmp_id_47ee7be0_fk_ppmp_ppmp_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ppmp_ppmp_key_log
    ADD CONSTRAINT ppmp_ppmp_key_log_ppmp_id_47ee7be0_fk_ppmp_ppmp_id FOREIGN KEY (ppmp_id) REFERENCES public.ppmp_ppmp(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.ppmp_ppmp_key_log DROP CONSTRAINT ppmp_ppmp_key_log_ppmp_id_47ee7be0_fk_ppmp_ppmp_id;
       public          eSmooothiee    false    249    258    3388            k           2606    20488 D   ppmp_ppmp_key_log ppmp_ppmp_key_log_user_id_2ef306ff_fk_auth_user_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ppmp_ppmp_key_log
    ADD CONSTRAINT ppmp_ppmp_key_log_user_id_2ef306ff_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.ppmp_ppmp_key_log DROP CONSTRAINT ppmp_ppmp_key_log_user_id_2ef306ff_fk_auth_user_id;
       public          eSmooothiee    false    3331    220    258            d           2606    19574 ;   ppmp_ppmp ppmp_ppmp_sof_id_4609932c_fk_ppmp_sourceoffund_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ppmp_ppmp
    ADD CONSTRAINT ppmp_ppmp_sof_id_4609932c_fk_ppmp_sourceoffund_id FOREIGN KEY (sof_id) REFERENCES public.ppmp_sourceoffund(id) DEFERRABLE INITIALLY DEFERRED;
 e   ALTER TABLE ONLY public.ppmp_ppmp DROP CONSTRAINT ppmp_ppmp_sof_id_4609932c_fk_ppmp_sourceoffund_id;
       public          eSmooothiee    false    249    243    3379            `           2606    20460 N   ppmp_ppmptrack ppmp_ppmptrack_orderdetails_id_2ac018eb_fk_ppmp_orderdetails_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ppmp_ppmptrack
    ADD CONSTRAINT ppmp_ppmptrack_orderdetails_id_2ac018eb_fk_ppmp_orderdetails_id FOREIGN KEY (orderdetails_id) REFERENCES public.ppmp_orderdetails(id) DEFERRABLE INITIALLY DEFERRED;
 x   ALTER TABLE ONLY public.ppmp_ppmptrack DROP CONSTRAINT ppmp_ppmptrack_orderdetails_id_2ac018eb_fk_ppmp_orderdetails_id;
       public          eSmooothiee    false    239    241    3372            b           2606    18485 C   ppmp_prices ppmp_prices_item_id_41ceca26_fk_ppmp_itemdescription_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ppmp_prices
    ADD CONSTRAINT ppmp_prices_item_id_41ceca26_fk_ppmp_itemdescription_id FOREIGN KEY (item_id) REFERENCES public.ppmp_itemdescription(id) DEFERRABLE INITIALLY DEFERRED;
 m   ALTER TABLE ONLY public.ppmp_prices DROP CONSTRAINT ppmp_prices_item_id_41ceca26_fk_ppmp_itemdescription_id;
       public          eSmooothiee    false    3368    247    237            a           2606    18480 P   ppmp_purchaserequest ppmp_purchaserequest_order_details_id_ecafbd38_fk_ppmp_orde    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ppmp_purchaserequest
    ADD CONSTRAINT ppmp_purchaserequest_order_details_id_ecafbd38_fk_ppmp_orde FOREIGN KEY (order_details_id) REFERENCES public.ppmp_orderdetails(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.ppmp_purchaserequest DROP CONSTRAINT ppmp_purchaserequest_order_details_id_ecafbd38_fk_ppmp_orde;
       public          eSmooothiee    false    3372    239    245           