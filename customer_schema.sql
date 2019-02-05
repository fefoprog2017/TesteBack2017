CREATE TABLE tb_customer_account (
	id_customer INTEGER PRIMARY KEY,
	cpf_cnpj integer NOT NULL,
	nm_customer VARCHAR(255) NOT NULL,
	is_active boolean NOT NULL,
	vl_total long NOT NULL
);