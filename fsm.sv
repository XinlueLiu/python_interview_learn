module !TODO! (
	input logic clk;
	input logic n_rst;

	!TODO!

);
	typedef enum logic [0:0] {luelue} state_t;

	state_t state;
	state_t next_state;

	always_ff @( posedge clk, negedge n_rst ) begin
		if (n_rst == '0) begin
			state <= luelue;
		end else begin
			state <= next_state;
		end
	end

	// next state logic
	always_comb begin
		next_state = state;
		case (state)
			luelue: begin
				if (apple) begin
					next_state = chongchongchong;
				end
			end
			end
		endcase
	end

	// output logic
	always_comb begin
	!TODO!
	end

endmodule
