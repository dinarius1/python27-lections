--
-- PostgreSQL database dump
--

-- Dumped from database version 14.7 (Ubuntu 14.7-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.7 (Ubuntu 14.7-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: authobiograohy; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.authobiograohy (
    id integer NOT NULL,
    published date,
    body text,
    author_id integer
);


ALTER TABLE public.authobiograohy OWNER TO "user";

--
-- Name: authobiograohy_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.authobiograohy_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.authobiograohy_id_seq OWNER TO "user";

--
-- Name: authobiograohy_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.authobiograohy_id_seq OWNED BY public.authobiograohy.id;


--
-- Name: author; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.author (
    id integer NOT NULL,
    name character varying(50),
    last_name character varying(70),
    year date
);


ALTER TABLE public.author OWNER TO "user";

--
-- Name: author_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.author_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.author_id_seq OWNER TO "user";

--
-- Name: author_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.author_id_seq OWNED BY public.author.id;


--
-- Name: blog; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.blog (
    id integer NOT NULL,
    name character varying(50),
    email character varying(70),
    age integer
);


ALTER TABLE public.blog OWNER TO "user";

--
-- Name: blog_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.blog_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.blog_id_seq OWNER TO "user";

--
-- Name: blog_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.blog_id_seq OWNED BY public.blog.id;


--
-- Name: blogger; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.blogger (
    id integer NOT NULL,
    name character varying(50),
    email character varying(70),
    age integer
);


ALTER TABLE public.blogger OWNER TO "user";

--
-- Name: blogger_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.blogger_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.blogger_id_seq OWNER TO "user";

--
-- Name: blogger_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.blogger_id_seq OWNED BY public.blogger.id;


--
-- Name: dev_proj; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.dev_proj (
    dev_id integer,
    proj_id integer
);


ALTER TABLE public.dev_proj OWNER TO "user";

--
-- Name: developer; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.developer (
    id integer NOT NULL,
    name character varying(50),
    age integer,
    experience integer
);


ALTER TABLE public.developer OWNER TO "user";

--
-- Name: developer_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.developer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.developer_id_seq OWNER TO "user";

--
-- Name: developer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.developer_id_seq OWNED BY public.developer.id;


--
-- Name: post; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.post (
    id integer NOT NULL,
    title character varying(100),
    body text,
    bloger_id integer
);


ALTER TABLE public.post OWNER TO "user";

--
-- Name: post_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.post_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.post_id_seq OWNER TO "user";

--
-- Name: post_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.post_id_seq OWNED BY public.post.id;


--
-- Name: project; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.project (
    id integer NOT NULL,
    title character varying(100),
    tz text,
    deadline date
);


ALTER TABLE public.project OWNER TO "user";

--
-- Name: project_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.project_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.project_id_seq OWNER TO "user";

--
-- Name: project_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.project_id_seq OWNED BY public.project.id;


--
-- Name: authobiograohy id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.authobiograohy ALTER COLUMN id SET DEFAULT nextval('public.authobiograohy_id_seq'::regclass);


--
-- Name: author id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.author ALTER COLUMN id SET DEFAULT nextval('public.author_id_seq'::regclass);


--
-- Name: blog id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.blog ALTER COLUMN id SET DEFAULT nextval('public.blog_id_seq'::regclass);


--
-- Name: blogger id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.blogger ALTER COLUMN id SET DEFAULT nextval('public.blogger_id_seq'::regclass);


--
-- Name: developer id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.developer ALTER COLUMN id SET DEFAULT nextval('public.developer_id_seq'::regclass);


--
-- Name: post id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.post ALTER COLUMN id SET DEFAULT nextval('public.post_id_seq'::regclass);


--
-- Name: project id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.project ALTER COLUMN id SET DEFAULT nextval('public.project_id_seq'::regclass);


--
-- Data for Name: authobiograohy; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.authobiograohy (id, published, body, author_id) FROM stdin;
1	2005-12-12	some bio	2
2	2003-03-13	some bio	3
\.


--
-- Data for Name: author; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.author (id, name, last_name, year) FROM stdin;
1	author1	aaa1	1995-12-30
2	author2	bbb2	1980-05-04
3	author3	cccc2	1978-08-13
\.


--
-- Data for Name: blog; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.blog (id, name, email, age) FROM stdin;
\.


--
-- Data for Name: blogger; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.blogger (id, name, email, age) FROM stdin;
1	bloger 1	aa@gmail.com	23
2	bloger 2	bb@gmail.com	18
3	bloger 3	ccc@gmail.com	26
4	bloger 4	gggg@gmail.com	23
\.


--
-- Data for Name: dev_proj; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.dev_proj (dev_id, proj_id) FROM stdin;
1	2
2	2
3	1
\.


--
-- Data for Name: developer; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.developer (id, name, age, experience) FROM stdin;
1	dev1	23	3
2	dev2	19	1
3	dev3	32	10
\.


--
-- Data for Name: post; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.post (id, title, body, bloger_id) FROM stdin;
1	post 1	...	3
2	post 2	aaa	2
3	post 3	---	1
4	post 4	aaaa	1
\.


--
-- Data for Name: project; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.project (id, title, tz, deadline) FROM stdin;
1	proj1	....	2023-02-12
2	proj2	....	2024-02-12
3	proj3	....	2023-03-12
\.


--
-- Name: authobiograohy_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.authobiograohy_id_seq', 2, true);


--
-- Name: author_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.author_id_seq', 3, true);


--
-- Name: blog_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.blog_id_seq', 1, false);


--
-- Name: blogger_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.blogger_id_seq', 4, true);


--
-- Name: developer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.developer_id_seq', 3, true);


--
-- Name: post_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.post_id_seq', 4, true);


--
-- Name: project_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.project_id_seq', 3, true);


--
-- Name: authobiograohy authobiograohy_author_id_key; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.authobiograohy
    ADD CONSTRAINT authobiograohy_author_id_key UNIQUE (author_id);


--
-- Name: author author_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.author
    ADD CONSTRAINT author_pkey PRIMARY KEY (id);


--
-- Name: blogger blogger_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.blogger
    ADD CONSTRAINT blogger_pkey PRIMARY KEY (id);


--
-- Name: developer developer_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.developer
    ADD CONSTRAINT developer_pkey PRIMARY KEY (id);


--
-- Name: project project_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.project
    ADD CONSTRAINT project_pkey PRIMARY KEY (id);


--
-- Name: authobiograohy fk_author_bio; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.authobiograohy
    ADD CONSTRAINT fk_author_bio FOREIGN KEY (author_id) REFERENCES public.author(id);


--
-- Name: dev_proj fk_dev_m2m; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.dev_proj
    ADD CONSTRAINT fk_dev_m2m FOREIGN KEY (dev_id) REFERENCES public.developer(id);


--
-- Name: post fk_post_blogger; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.post
    ADD CONSTRAINT fk_post_blogger FOREIGN KEY (bloger_id) REFERENCES public.blogger(id);


--
-- Name: dev_proj fk_proj_m2m; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.dev_proj
    ADD CONSTRAINT fk_proj_m2m FOREIGN KEY (proj_id) REFERENCES public.project(id);


--
-- PostgreSQL database dump complete
--



