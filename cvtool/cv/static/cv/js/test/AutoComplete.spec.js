import {AutoComplete} from './AutoComplete';
describe('AutoComplete', () => {
	it('shows existing entries in the system', () => {
		const ac = new AutoComplete()
		expect(ac.test()).toBe('test');
	});
});