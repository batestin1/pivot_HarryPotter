CREATE TABLE public.harrypotter (
	id serial NOT NULL,
	name text NULL,
	gender text NULL,
	adress text NULL,
	houses text NULL,
	wand text NULL,
	patronus text NULL,
	birth date NULL,
	occupation text NULL,
	dt_update timestamp NULL,
	CONSTRAINT customers_pkey PRIMARY KEY (id)
);

